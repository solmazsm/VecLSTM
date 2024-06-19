;==========================================
; Title: Create a table to store VecLSTM_trajectory_prediction
; Author: anonymous - ICDM 2024 - conference
; Date:   ICDM 2024
;==========================================

create_table_query = 
CREATE TABLE IF NOT EXISTS trajectory_predictions (
    metadata VARCHAR(255),
    prediction FLOAT
)
