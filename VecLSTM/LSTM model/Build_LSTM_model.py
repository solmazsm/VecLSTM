;==========================================
; Title: Build_LSTM_model
; Author: anonymous - ECML PKDD 2024 - conference
; Date:   21 March 2024
;==========================================

model = Sequential()
model.add(LSTM(units=100, input_shape=(X_train_scaled_reshaped.shape[1], X_train_scaled_reshaped.shape[2]), return_sequences=True))
model.add(LSTM(units=50, return_sequences=False))  
model.add(Dense(units=num_classes, activation='softmax'))
