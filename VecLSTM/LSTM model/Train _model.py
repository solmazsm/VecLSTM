;==========================================
; Title: Train the model with class weights
; Author: anonymous - ECML PKDD 2024 - conference
; Date:   21 March 2024
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
