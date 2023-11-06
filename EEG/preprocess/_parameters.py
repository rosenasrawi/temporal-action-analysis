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


# Files
files = {
    'eeg': []
}

for sub in subjects:

    sub_file = []
    
    for ses in sessions:
    
        file = '/eeg_s' + str(sub) + ses + '.bdf'
        sub_file.append(dirs['home'] + dirs['eeg'] + file)

    files['eeg'].append(sub_file)

# Channels
channels = {
    'drop': ['EXG1', 'EXG2', 'GSR1', 'GSR2', 'Erg1', 'Erg2', 'Resp', 'Plet', 'Temp'],
    'ref': ['EXG1', 'EXG2']
}

# Triggers
triggers = {
    'enc1': list(range(1,9))
}