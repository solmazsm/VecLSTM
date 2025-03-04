;==========================================
; Title: Insert trajectory predictions into a MySQL table
; Author: Solmaz Seyed Monir
;==========================================
for index, row in df_predictions.iterrows():
    query = f"INSERT INTO trajectory_predictions (metadata, prediction) VALUES ('{row['Metadata']}', {row['Prediction']})"
    cursor.execute(query)
