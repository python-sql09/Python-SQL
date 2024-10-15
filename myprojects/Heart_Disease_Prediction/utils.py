# utils.py
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class ModelEvaluator:
    def evaluate_model(self, y_test, predictions):
        accuracy = accuracy_score(y_test, predictions)
        print("Accuracy:", accuracy)
        print("Classification Report:\n", classification_report(y_test, predictions))
        print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))