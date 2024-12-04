;==========================================
; Title: Insert trajectory predictions into a MySQL table
; Author: anonymous
;==========================================
for index, row in df_predictions.iterrows():
    query = f"INSERT INTO trajectory_predictions (metadata, prediction) VALUES ('{row['Metadata']}', {row['Prediction']})"
    cursor.execute(query)
