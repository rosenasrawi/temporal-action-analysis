# Subs
subjects = list(range(1,6))
sessions = ['a','b']

# Directories

dirs = {
    'home':  '/Users/rosenasrawi/Documents/VU PhD/Projects/rn6 - Temporal action',
    'data': '/Users/rosenasrawi/Documents/VU PhD/Projects/rn6 - Temporal action/Data'
}

dirs['eeg'] = dirs['data'] + '/lab/EEG'
dirs['log'] = dirs['data'] + '/lab/log'
dirs['raw'] = dirs['data'] + '/processed/raw'
dirs['ica'] = dirs['data'] + '/processed/ica'
dirs['epoch'] = dirs['data'] + '/processed/epoch'
dirs['tfr'] = dirs['data'] + '/processed/tfr'
dirs['cvsi'] = dirs['data'] + '/processed/cvsi'

# Channels
channels = {
    'drop': ['EXG1', 'EXG2', 'GSR1', 'GSR2', 'Erg1', 'Erg2', 'Resp', 'Plet', 'Temp'],
    'ref': ['EXG1', 'EXG2']
}

# Triggers
triggers = {
    'enc1': list(range(1,9))
}

# Event dict

event_id = {
    'same/itemL/respL': 1,
    'same/itemL/respR': 2,
    'same/itemR/respL': 3,
    'same/itemR/respR': 4,
    'rvrs/itemL/respL': 5,
    'rvrs/itemL/respR': 6,
    'rvrs/itemR/respL': 7,
    'rvrs/itemR/respR': 8,
}

# Conditions

cond = {
    'visual': ['same/itemL', 'same/itemR', 
               'rvrs/itemL', 'rvrs/itemR'],
    'motor': ['same/respL', 'same/respR', 
              'rvrs/respL', 'rvrs/respR']
}
