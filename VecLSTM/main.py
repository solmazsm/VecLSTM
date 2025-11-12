from fastapi import FastAPI, HTTPException
import mysql.connector
import os
import json
from pydantic import BaseModel

app = FastAPI()


class EmbeddingPayload(BaseModel):
    user_id: int
    start_time: str  
    end_time: str    
    transport_mode: str
    avg_speed: float
    vectorized_tensor: list
    label: int
    source_dataset: str = None

def get_db_conn():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', ''),
        database=os.getenv('MYSQL_DB', 'veclstm_db')
    )

@app.post("/store_embedding/")
def store_embedding(payload: EmbeddingPayload):
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            INSERT INTO veclstm_trajectories 
            (user_id, start_time, end_time, transport_mode, avg_speed, vectorized_tensor, label, source_dataset)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                payload.user_id,
                payload.start_time,
                payload.end_time,
                payload.transport_mode,
                payload.avg_speed,
                json.dumps(payload.vectorized_tensor),
                payload.label,
                payload.source_dataset
            )
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"DB Error: {e}")
    finally:
        cur.close()
        conn.close()
    return {"status": "ok", "message": "Embedding stored successfully"}


@app.get("/")
def read_root():
    return {"message": "VecLSTM API running."}






