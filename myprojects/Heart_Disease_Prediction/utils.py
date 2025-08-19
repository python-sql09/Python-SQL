# utils.py
# --------------------------------------------------------------------------------------
# Project Name: Heart Disease Prediction
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      :https://github.com/python-sql09/Python-SQL/tree/main/myprojects/Heart_Disease_Prediction
# Date        :March 27, 2024 to May 3, 2024
# Description : This project applies data preprocessing, feature engineering, and multiple machine learning
#               algorithms to compare performance and identify the best predictive model.
# ----------------------------------------------------------------------------------------
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class ModelEvaluator:
    def __init__(self):
        self.results = []

    def evaluate_model(self, y_true, y_pred, model_name):
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)

        self.results.append({
            "Model": model_name,
            "Accuracy": accuracy,
            "Precision": precision,
            "Recall": recall,
            "F1 Score": f1
        })

    def get_results_dataframe(self):
        return pd.DataFrame(self.results)

    def print_results(self):
        results_df = pd.DataFrame(self.results)
        print(results_df)