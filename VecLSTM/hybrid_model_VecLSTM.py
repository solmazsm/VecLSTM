# Create a model that includes both LSTM and CNN

model = Model(inputs=[model_without_vectorization.input, cnn_model.input], outputs=combined_model)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
