
;==========================================
; Title: Trajectory Data Processing and Labeling
; Author: Solmaz Seyed Monir
;==========================================

mode_names = ['walk', 'bike', 'bus', 'car', 'subway','train', 'airplane', 'boat', 'run', 'motorcycle', 'taxi']
mode_ids = {s : i + 1 for i, s in enumerate(mode_names)}
print(mode_ids)
def read_labels(labels_file):
    labels = pd.read_csv(labels_file, skiprows=1, header=None,
                         parse_dates=[[0, 1], [2, 3]],
                         infer_datetime_format=True, delim_whitespace=True)

   
    labels.columns = ['start_time', 'end_time', 'label']


    labels['label'] = [mode_ids[i] for i in labels['label']]
    
    return labels

