# Subs
subjects = list(range(1,9)) + list(range(10, 27))
sessions = ['a','b']

# Directories

dirs = {
    'home':  '/Users/rosenasrawi/Documents/VU PhD/Projects/rn6 - Temporal action',
    'data': '/Users/rosenasrawi/Documents/VU PhD/Projects/rn6 - Temporal action/Data'
}

dirs['eeg'] = dirs['data'] + '/lab/EEG'
dirs['log'] = dirs['data'] + '/lab/logfiles'
dirs['raw'] = dirs['data'] + '/processed/raw'
dirs['ica'] = dirs['data'] + '/processed/ica'
dirs['epoch'] = dirs['data'] + '/processed/epoch'
dirs['tfr'] = dirs['data'] + '/processed/tfr'
dirs['cvsi'] = dirs['data'] + '/processed/cvsi'
dirs['stat'] = dirs['data'] + '/processed/stat'

dirs['plot'] = dirs['home'] + '/Plot'

# Channels
channels = {
    'drop': ['EXG1', 'EXG2', 'GSR1', 'GSR2', 'Erg1', 'Erg2', 'Resp', 'Plet', 'Temp'],
    'ref': ['EXG1', 'EXG2']
}

bad_channels = {
    1: [''],
    2: ['P2','PO4'],
    3: ['P6','PO4','PO8'],
    4: ['PO3'],
    5: ['P2'],
    6: ['P2'],
    7: ['P2'],
    8: ['P2'],
    9: ['PO4'],
    10: ['P2'],
    11: [''],
    12: ['P2', 'P4'],
    13: ['P2'],
    14: [''],
    15: ['P2'],
    16: ['P2', 'FT8'],
    17: ['P2'],
    18: ['P2','PO4', 'O2', 'PO7'],
    19: [''],
    20: [''],
    21: ['P2','PO4'],
    22: [''],
    23: ['P2','PO4', 'P4'],
    24: ['POz'],
    25: ['P2'],
    26: ['P2']
}

# Triggers
triggers = {
    'enc1': list(range(1,9)),
    'prob1': list(range(21,29)),
    'prob2': list(range(51,59)),
    'resp1': list(range(31,49)),
    'resp2': list(range(61,79)),
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

resp_id = {
    'same/itemL/respL': 1,
    'same/itemL/respR': 2,
    'same/itemR/respL': 3,
    'same/itemR/respR': 4,
    'rvrs/itemR/respR': 5,
    'rvrs/itemR/respL': 6,
    'rvrs/itemL/respR': 7,
    'rvrs/itemL/respL': 8,
}

probe1_id = resp_id.copy()
probe2_id = resp_id.copy()

for key in resp_id:
    probe1_id[key] += 20
    probe2_id[key] += 50

resp1 = [30,40,30,40,40,30,40,30]
resp2 = [70,60,70,60,60,70,60,70]

resp1_id = resp_id.copy()
resp2_id = resp_id.copy()

for i, key in enumerate(resp_id):
    resp1_id[key] += resp1[i]
    resp2_id[key] += resp2[i]

# Time-windows
    
time_window = {
    'enc1': [-1,4],
    'prob1': [-1,3],
    'prob2': [-3,3],
    'resp1': [-1,3],
    'resp2': [-3,3]
}

# Conditions

cond = {
    'visual': ['itemL', 'itemR'],
    'vis-samerev': ['same/itemL', 'same/itemR', 
                    'rvrs/itemL', 'rvrs/itemR'],

    'motor': ['respL', 'respR'],
    'mot-samerev': ['same/respL', 'same/respR', 
                    'rvrs/respL', 'rvrs/respR']
}

# Plot colors

palette ={
    'blue': '#96bfe6',
    'green': '#8cdea1',
    'orange': '#ff7340',
    'yellow': '#facf73',
    'grey': '#999999'
}