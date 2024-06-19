# Build the CNN model

cnn_model = Sequential()
cnn_model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(X_train_resampled.shape[1], 1)))
cnn_model.add(MaxPooling1D(pool_size=1))  # Adjust pool size to 1
cnn_model.add(Flatten())
