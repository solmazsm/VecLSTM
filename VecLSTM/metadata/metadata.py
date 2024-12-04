;==========================================
; Title: Create metadata
; Author: anonymous 
;==========================================

metadata_list = [f"{trajectory_id}_{point}" for trajectory_id, trajectory in enumerate(trajectories) for point in range(len(trajectory))]

# Create labels and metadata
df_true_labels = pd.DataFrame({'Metadata': metadata_list, 'TrueLabel': labels_list})
