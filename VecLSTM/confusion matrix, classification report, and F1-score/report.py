;==========================================
; Title: confusion matrix, classification report, and F1-score
; Author: anonymous 
;==========================================
conf_matrix = confusion_matrix(np.argmax(y_test_encoded, axis=1), predictions_array)
classification_rep = classification_report(np.argmax(y_test_encoded, axis=1), predictions_array)
f1 = f1_score(np.argmax(y_test_encoded, axis=1), predictions_array, average='weighted')

