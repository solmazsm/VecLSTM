;==========================================
; Title: Create a table to store VecLSTM_trajectory_prediction
; Author: anonymous 
; Date:   The Web Conference 2025
;==========================================

create_table_query = 
CREATE TABLE IF NOT EXISTS trajectory_predictions (
    metadata VARCHAR(255),
    prediction FLOAT
)
