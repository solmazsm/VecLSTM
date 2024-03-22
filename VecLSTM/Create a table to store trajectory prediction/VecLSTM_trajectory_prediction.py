;==========================================
; Title: Create a table to store VecLSTM_trajectory_prediction
; Author: anonymous - ECML PKDD 2024 - conference
; Date:   21 March 2024
;==========================================

create_table_query = 
CREATE TABLE IF NOT EXISTS trajectory_predictions (
    metadata VARCHAR(255),
    prediction FLOAT
)
