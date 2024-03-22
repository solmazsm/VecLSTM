Insert trajectory predictions into a MySQL table
;==========================================
; Title: Insert trajectory predictions into a MySQL table
; Author: 
; Date:  21 March 2024
;==========================================
for index, row in df_predictions.iterrows():
    query = f"INSERT INTO trajectory_predictions (metadata, prediction) VALUES ('{row['Metadata']}', {row['Prediction']})"
    cursor.execute(query)
