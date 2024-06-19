# Make predictions using the combined model on the test set
y_pred = model.predict([X_test_resampled, X_test_resampled])
y_pred_labels = np.argmax(y_pred, axis=1)
