;==========================================
; Title: Train the model with class weights
; Author: anonymous 
; Date:    The Web Conference 2025
;==========================================

history = model.fit(
    X_train_scaled_reshaped,
    y_train_encoded,
    epochs=20,  
    batch_size=64,
    validation_split=0.2,
    callbacks=[early_stopping],
    class_weight=class_weight_dict
)
