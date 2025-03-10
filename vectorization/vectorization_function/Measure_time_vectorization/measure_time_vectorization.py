;==========================================
; Title: Measure the time for vectorization
; Author: Solmaz Seyed Monir
;==========================================
# With Vectorization
    # Measure the time for vectorization
    start_time_vectorization = time.time()

   
    vectorized_data_array = np.zeros((len(trajectories), 10, 10, len(trajectories[0][0])))

    for i, trajectory in enumerate(trajectories):
        vectorized_data_array[i] = vectorization_function_VecLSTM(trajectory)

   
    end_time_vectorization = time.time()
    vectorization_time = end_time_vectorization - start_time_vectorization

   
   
