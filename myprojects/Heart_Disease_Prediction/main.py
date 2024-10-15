# main.py
from data_preprocessing import DataProcessor
from model_training import ModelTrainer
from utils import ModelEvaluator
import pandas as pd
import numpy as np

# Initialize the classes
data_processor = DataProcessor()
model_trainer = ModelTrainer()
model_evaluator = ModelEvaluator()

# Load the data
data = pd.read_csv("/home/deepa3/python-sql09/Python-SQL/myprojects/Heart_Disease_Prediction/processed_cleveland.data", header=None)
data.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 
                'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']  # Adjust as per your dataset

# Clean the data
data.replace('?', np.nan, inplace=True)  # Replace '?' with NaN
data = data.apply(pd.to_numeric, errors='coerce')  # Convert all columns to numeric
data.dropna(inplace=True)  # Drop rows with any NaN values

print(data.columns)
print(data.head())

# Preprocess data
X_train, X_test, y_train, y_test = data_processor.preprocess_data(data)

# Train and evaluate models
# Logistic Regression
logistic_preds = model_trainer.train_logistic_regression(X_train, y_train, X_test)
print("Logistic Regression:")
model_evaluator.evaluate_model(y_test, logistic_preds)

# Random Forest with StandardScaler
rf_standard_preds = model_trainer.train_random_forest(X_train, y_train, X_test, scale_type="standard")
print("\nRandom Forest (StandardScaler):")
model_evaluator.evaluate_model(y_test, rf_standard_preds)

# Random Forest with MinMaxScaler
rf_minmax_preds = model_trainer.train_random_forest(X_train, y_train, X_test, scale_type="minmax")
print("\nRandom Forest (MinMaxScaler):")
model_evaluator.evaluate_model(y_test, rf_minmax_preds)

# XGBoost
xgb_preds = model_trainer.train_xgboost(X_train, y_train, X_test)
print("\nXGBoost:")
model_evaluator.evaluate_model(y_test, xgb_preds)

# Support Vector Machine
svm_preds = model_trainer.train_svm(X_train, y_train, X_test)
print("\nSupport Vector Machine:")
model_evaluator.evaluate_model(y_test, svm_preds)

# K-Nearest Neighbors
knn_preds = model_trainer.train_knn(X_train, y_train, X_test)
print("\nK-Nearest Neighbors:")
model_evaluator.evaluate_model(y_test, knn_preds)

# Naive Bayes
nb_preds = model_trainer.train_naive_bayes(X_train, y_train, X_test)
print("\nNaive Bayes:")
model_evaluator.evaluate_model(y_test, nb_preds)