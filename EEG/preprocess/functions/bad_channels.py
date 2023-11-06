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