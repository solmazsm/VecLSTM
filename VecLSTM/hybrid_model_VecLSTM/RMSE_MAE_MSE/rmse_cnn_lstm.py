# RMSE
rmse_cnn_lstm = np.sqrt(np.mean((y_pred_laabels - np.argmax(y_test_encoded, axis=1)) ** 2))
