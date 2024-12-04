;==========================================
; Title: Compile_the_model_without_vectorization
; Author: anonymous 
;==========================================

    model_without_vectorization = Sequential()
    model_without_vectorization.add(LSTM(100, input_shape=(X_train_resampled.shape[1], 1), activation='relu', return_sequences=True))
    model_without_vectorization.add(LSTM(50, activation='relu'))
    model_without_vectorization.add(Dense(num_classes, activation='softmax'))

    # Compile the model
    model_without_vectorization.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
