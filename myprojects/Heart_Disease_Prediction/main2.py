from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd

class ModelTrainer:
    def train_logistic_regression(self, X_train, y_train, X_test, max_iter=1000):
        model = LogisticRegression(max_iter=max_iter)
        model.fit(X_train, y_train)
        return model.predict(X_test)

    def train_random_forest(self, X_train, y_train, X_test, scale_type=None):
        if scale_type == "standard":
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)
        elif scale_type == "minmax":
            scaler = MinMaxScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)

        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        return model.predict(X_test)

    def train_xgboost(self, X_train, y_train, X_test):
        model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
        model.fit(X_train, y_train)
        return model.predict(X_test)

    def train_svm(self, X_train, y_train, X_test):
        model = SVC()
        model.fit(X_train, y_train)
        return model.predict(X_test)

    def train_knn(self, X_train, y_train, X_test):
        model = KNeighborsClassifier()
        model.fit(X_train, y_train)
        return model.predict(X_test)

    def train_naive_bayes(self, X_train, y_train, X_test):
        model = GaussianNB()
        model.fit(X_train, y_train)
        return model.predict(X_test)

    def plot_model_performance(self, results_df):
        """
        Plot the performance of different models.

        Parameters:
        results_df (DataFrame): DataFrame containing model evaluation metrics
        """
        plt.figure(figsize=(10, 6))
        plt.barh(results_df['Model'], results_df['Accuracy'], color='skyblue')
        plt.xlabel('Accuracy')
        plt.title('Model Performance Comparison')
        plt.xlim(0, 1)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.show()

# Example usage of the ModelTrainer class
if __name__ == "__main__":
    # Assume you have prepared your X_train, y_train, X_test data here
    trainer = ModelTrainer()

    # Train different models
    predictions_logistic = trainer.train_logistic_regression(X_train, y_train, X_test)
    predictions_rf = trainer.train_random_forest(X_train, y_train, X_test, scale_type='standard')
    predictions_xgb = trainer.train_xgboost(X_train, y_train, X_test)
    predictions_svm = trainer.train_svm(X_train, y_train, X_test)
    predictions_knn = trainer.train_knn(X_train, y_train, X_test)
    predictions_nb = trainer.train_naive_bayes(X_train, y_train, X_test)

    # Assume you have a function to calculate metrics
    # metrics_df = calculate_metrics(y_test, [predictions_logistic, predictions_rf, predictions_xgb, predictions_svm, predictions_knn, predictions_nb])

    # For example, create a DataFrame with results
    results = {
        'Model': ['Logistic Regression', 'Random Forest', 'XGBoost', 'SVM', 'KNN', 'Naive Bayes'],
        'Accuracy': [0.6, 0.57, 0.56, 0.53, 0.48, 0.55],  # Replace with actual accuracy values
        'Precision': [0.57, 0.43, 0.51, 0.28, 0.31, 0.54],  # Example values
        'Recall': [0.60, 0.57, 0.57, 0.53, 0.48, 0.55],  # Example values
        'F1 Score': [0.55, 0.49, 0.53, 0.37, 0.38, 0.54]  # Example values
    }
    results_df = pd.DataFrame(results)

    # Plot model performance
    trainer.plot_model_performance(results_df)