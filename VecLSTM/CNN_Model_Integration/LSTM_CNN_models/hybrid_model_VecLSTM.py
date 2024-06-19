# Concatenate LSTM and CNN outputs

combined_model = concatenate([model_without_vectorization.output, cnn_model.output])
combined_model = Dense(num_classes, activation='softmax')(combined_model)
