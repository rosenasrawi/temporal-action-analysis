# Subs
subjects = list(range(1,6))
sessions = ['a','b']

# Directories
dirs = {
    'home': '/Users/rosenasrawi/Documents/VU PhD/Projects/rn6 - Temporal action',
    'eeg': '/Data/lab/EEG',
    'log': '/Data/lab/logfiles',
    'raw': '/Data/processed/raw',
    'ica': '/Data/processed/ica'
}

# Files
files = {
    'eeg': []
}

for sub in subjects:

    sub_file = []
    
    for ses in sessions:
    
        file = '/rn6_s' + str(sub) + ses + '.bdf'
        sub_file.append(dirs['home'] + dirs['eeg'] + file)

    files['eeg'].append(sub_file)

# Channels

channels = {
    'drop': ['EXG1', 'EXG2', 'GSR1', 'GSR2', 'Erg1', 'Erg2', 'Resp', 'Plet', 'Temp'],
    'ref': ['EXG1', 'EXG2']
}

# Triggers