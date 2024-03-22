;==========================================
; Title: Function to load trajector_VecLSTM
; Author: 
; Date:   21 March 2024
;==========================================

def load_trajectory_from_df(trajectory_df):
  
    trajectory_df = trajectory_df.rename(columns={1: 'Latitude', 2: 'Longitude', 3: 'Altitude'})
    
   
    trajectory_df['Latitude'] = pd.to_numeric(trajectory_df['Latitude'], errors='coerce')
    trajectory_df['Longitude'] = pd.to_numeric(trajectory_df['Longitude'], errors='coerce')
    
    
    trajectory_df = trajectory_df.dropna(subset=['Latitude', 'Longitude'])
    
  
    trajectory = trajectory_df[['Latitude', 'Longitude', 'Altitude']].values
    return trajectory
