;==========================================
; Title: vectorization process
; Author: anonymous - ICDM 2024 - conference
; Date:   ICDM 2024
;======
def VecLSTM_vectorization(lat_lon_alt):
   
    if np.any(np.isnan(lat_lon_alt)) or np.any(np.isinf(lat_lon_alt)):
        raise ValueError("Input data contains NaN or infinite values.")

    # Assuming lat_lon_alt is a 2D array (latitude, longitude)
    # Normalize each dimension to the range [0, 1]
    normalized_data = (lat_lon_alt - lat_lon_alt.min(axis=0)) / (lat_lon_alt.max(axis=0) - lat_lon_alt.min(axis=0))

  
    normalized_data = np.nan_to_num(normalized_data, nan=0.5)

   
    if np.any(np.isnan(normalized_data)) or np.any(np.isinf(normalized_data)):
        print("Problematic trajectory:")
        print(lat_lon_alt)
        print("Normalized data:")
        print(normalized_data)
        raise ValueError("Normalized data contains NaN or infinite values.")

   
    vectorized_data = np.zeros((10, 10, normalized_data.shape[1]))
    for i in range(normalized_data.shape[1]):
        vectorized_data[:, :, i] = np.histogram2d(normalized_data[:, i], np.arange(len(normalized_data)), bins=(10, 10))[0]

    return vectorized_data
