import mne
import numpy as np
import sails
import pandas as pd
from scipy import stats

def bad_channels(raw, picks, ref_meg="auto", sig_lev=0.05):
    """Set bad channels in MNE object.

    Parameters
    ----------
    raw : mne.Raw
        MNE raw object.
    picks : str
        Channel types to pick. Note that with CTF data, mne.pick_types will return:
        ~274 axial grads (as magnetometers) if {picks: 'mag', ref_meg: False}
        ~28 reference axial grads if {picks: 'grad'}.
    ref_meg : str
        ref_meg argument to pass with mne.pick_types().
    significance_level : float
        Significance level for detecting outliers. Must be between 0-1.

    Returns
    -------
    raw : mne.Raw
        MNE Raw object with bad channels marked.
    """

    gesd_args = {'alpha': sig_lev}

    if (picks == "mag") or (picks == "grad"):
        chinds = mne.pick_types(raw.info, meg=picks, ref_meg=ref_meg, exclude='bads')
    elif picks == "meg":
        chinds = mne.pick_types(raw.info, meg=True, ref_meg=ref_meg, exclude='bads')
    elif picks == "eeg":
        chinds = mne.pick_types(raw.info, eeg=True, ref_meg=ref_meg, exclude='bads')
    elif picks == "eog":
        chinds = mne.pick_types(raw.info, eog=True, ref_meg=ref_meg, exclude='bads')
    elif picks == "ecg":
        chinds = mne.pick_types(raw.info, ecg=True, ref_meg=ref_meg, exclude='bads')
    else:
        raise NotImplementedError(f"picks={picks} not available.")
    ch_names = np.array(raw.ch_names)[chinds]

    bdinds = sails.utils.detect_artefacts(
        raw.get_data(picks=chinds),
        axis=0,
        reject_mode="dim",
        ret_mode="bad_inds",
        gesd_args=gesd_args,
    )

    s = "Modality {0} - {1}/{2} channels rejected"
    print(s.format(picks, bdinds.sum(), len(bdinds)))

    print(ch_names[np.where(bdinds)[0]])

    # concatenate newly found bads to existing bads
    if np.any(bdinds):
        raw.info["bads"].extend(list(ch_names[np.where(bdinds)[0]]))

    return raw

def bad_epochs(
    epochs,
    picks,
    significance_level=0.05,
    max_percentage=0.1,
    outlier_side=0,
    metric='std',
    ref_meg='auto',
    mode=None,
):
    """Drop bad epochs in MNE object.
    Parameters
    ----------
    epochs : mne.Epochs
        MNE Epochs object.
    picks : str
        Channel types to pick. Note that with CTF data, mne.pick_types will return:
        ~274 axial grads (as magnetometers) if {picks: 'mag', ref_meg: False}
        ~28 reference axial grads if {picks: 'grad'}.
    significance_level : float
        Significance level for detecting outliers. Must be between 0-1.
    max_percentage : float
        Maximum fraction of the epochs to drop. Should be between 0-1.
    outlier_side : int
        Specify sidedness of the test:
       - outlier_side = -1 -> outliers are all smaller
       - outlier_side = 0  -> outliers could be small/negative or large/positive (default)
       - outlier_side = 1  -> outliers are all larger
    metric : str
        Metric to use. Could be 'std', 'var' or 'kurtosis'.
    ref_meg : str
        ref_meg argument to pass with mne.pick_types().
    mode : str
        Should be 'diff' or None. When mode='diff' we calculate a difference time
        series before detecting bad segments.
    Returns
    -------
    epochs : mne.Epochs
        MNE Epochs object with bad epoches dropped.
    """

    gesd_args = {
        'alpha': significance_level,
        'p_out': max_percentage,
        'outlier_side': outlier_side,
    }

    if (picks == "mag") or (picks == "grad"):
        chinds = mne.pick_types(epochs.info, meg=picks, ref_meg=ref_meg, exclude='bads')
    elif picks == "meg":
        chinds = mne.pick_types(epochs.info, meg=True, ref_meg=ref_meg, exclude='bads')
    elif picks == "eeg":
        chinds = mne.pick_types(epochs.info, eeg=True, ref_meg=ref_meg, exclude='bads')
    elif picks == "eog":
        chinds = mne.pick_types(epochs.info, eog=True, ref_meg=ref_meg, exclude='bads')
    elif picks == "ecg":
        chinds = mne.pick_types(epochs.info, ecg=True, ref_meg=ref_meg, exclude='bads')
    elif picks == "misc":
        chinds = mne.pick_types(epochs.info, misc=True, ref_meg=ref_meg, exclude='bads')
    else:
        raise NotImplementedError(f"picks={picks} not available.")

    if mode is None:
        X = epochs.get_data(picks=chinds)
    elif mode == "diff":
        X = np.diff(epochs.get_data(picks=chinds), axis=-1)

    # Get the function used to calculate the evaluation metric
    allowed_metrics = ["std", "var", "kurtosis"]
    if metric not in allowed_metrics:
        raise ValueError(f"metric {metric} unknown.")
    if metric == "std":
        metric_func = np.std
    elif metric == "var":
        metric_func = np.var
    else:
        metric_func = stats.kurtosis

    # Calculate the metric used to evaluate whether an epoch is bad
    X = metric_func(X, axis=-1)

    # Average over channels so we have a metric for each trial
    X = np.mean(X, axis=1)

    # Use gesd to find outliers
    bad_epochs, _ = sails.utils.gesd(X, **gesd_args)
    print(f"Modality {picks} - {np.sum(bad_epochs)}/{X.shape[0]} epochs rejected")

    # Drop bad epochs
    epochs.drop(bad_epochs)

    return epochs