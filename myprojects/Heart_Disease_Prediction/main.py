# main1.py
# --------------------------------------------------------------------------------------
# Project Name: Heart Disease Prediction
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      :https://github.com/python-sql09/Python-SQL/tree/main/myprojects/Heart_Disease_Prediction
# Date        :March 27, 2024 to May 3, 2024
# Description : This project applies data preprocessing, feature engineering, and multiple machine learning
#               algorithms to compare performance and identify the best predictive model.
# ----------------------------------------------------------------------------------------
from data_preprocessing import DataProcessor
from model_training import ModelTrainer
from utils import ModelEvaluator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Initialize the classes
data_processor = DataProcessor()
model_trainer = ModelTrainer()
model_evaluator = ModelEvaluator()

# Load the data
data_path = "processed_cleveland.data"
data = pd.read_csv(data_path, header=None)
data.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 
                'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# Clean the data
data.replace('?', np.nan, inplace=True)
data = data.apply(pd.to_numeric, errors='coerce')
data.dropna(inplace=True)

# Display basic information about the data
print(data.columns)
print(data.head())

# Preprocess data
X_train, X_test, y_train, y_test = data_processor.preprocess_data(data)

# Optionally, scale the data for better convergence
scaler = StandardScaler()  # or MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define a dictionary for models and their training functions
models = {
    "Logistic Regression": lambda X_train, y_train, X_test: model_trainer.train_logistic_regression(X_train, y_train, X_test, max_iter=10000),  # Increased max_iter
    "Random Forest (StandardScaler)": lambda X_train, y_train, X_test: model_trainer.train_random_forest(X_train, y_train, X_test, scale_type="standard"),
    "Random Forest (MinMaxScaler)": lambda X_train, y_train, X_test: model_trainer.train_random_forest(X_train, y_train, X_test, scale_type="minmax"),
    "XGBoost": model_trainer.train_xgboost,
    "Support Vector Machine": model_trainer.train_svm,
    "K-Nearest Neighbors": model_trainer.train_knn,
    "Naive Bayes": model_trainer.train_naive_bayes,
}

# Train and evaluate each model
for model_name, train_func in models.items():
    print(f"\nTraining and evaluating: {model_name}")
    predictions = train_func(X_train, y_train, X_test)
    
    # Evaluate the model
    model_evaluator.evaluate_model(y_test, predictions, model_name)

# Get results as a DataFrame
results_df = model_evaluator.get_results_dataframe()

# Display results as a table
print("\nModel Evaluation Results:")
model_evaluator.print_results()

# Set the color palette
sns.set_palette("pastel")  # You can choose other palettes like "bright", "muted", "dark", etc.

# Visualization of accuracy scores using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(data=results_df, x='Model', y='Accuracy', palette='viridis', hue='Model', dodge=False)  # Removed palette argument and hue
plt.legend(title='Models', loc='upper right')
plt.title('Model Accuracy Comparison')
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.grid(axis='y')

# Save the plot as an image
plt.tight_layout()
plt.savefig('model_accuracy_comparison.png')
plt.show()