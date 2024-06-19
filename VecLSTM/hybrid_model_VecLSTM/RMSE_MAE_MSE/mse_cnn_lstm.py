mse_cnn_lstm = np.mean((y_pred_labels - np.argmax(y_test_encoded, axis=1)) ** 2)
