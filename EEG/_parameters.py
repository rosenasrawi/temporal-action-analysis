

# Directories

dirs = {
    'home': '/Users/rosenasrawi/Documents/VU PhD/Projects/rn6 - Temporal action/',
    'eeg': 'Data/EEG/',
    'log': 'Data/logfiles/'
}

# Files

subjects = list(range(1,6))
sessions = ['a','b']

files = {
    'eeg': []
}

base = dirs['home'] + dirs['eeg']

for sub in subjects:

    for ses in sessions:
    
        file = 'rn6_s' + str(sub) + ses + '.bdf'
        files['eeg'].append(base + file)

# Triggers

