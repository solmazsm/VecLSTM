;==========================================
; Title: Train_the_model_without_vectorization
; Author: anonymous - ICDM 2024 - conference
; Date:   ICDM 2024
;==========================================

model_without_vectorization.fit(
        X_train_resampled,
        y_train_resampled,
        epochs=20, 
        batch_size=32,
        validation_data=(X_test_resampled, y_test_resampled)
    )
