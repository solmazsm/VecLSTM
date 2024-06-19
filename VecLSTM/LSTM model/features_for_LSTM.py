;==========================================
; Title: Reshape the input features for LSTM
; Author: 
; Date:   ICDM 2024
;==========================================

X_train_scaled_reshaped = X_train_scaled.reshape(-1, X_train_scaled.shape[1], 1)
X_test_scaled_reshaped = X_test_scaled.reshape(-1, X_test_scaled.shape[1], 1)
