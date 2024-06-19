# RMSE, MAE, and MSE
mae_cnn_lstm = np.mean(np.abs(y_pred_labels - np.argmax(y_test_encoded, axis=1)))
