#retrieve the data

retrieve_query = f"SELECT * FROM vectorized_data WHERE metadata='{metadata_list[0]}'"
cursor.execute(retrieve_query)
retrieved_vectorized_data_str = cursor.fetchone()[1]
