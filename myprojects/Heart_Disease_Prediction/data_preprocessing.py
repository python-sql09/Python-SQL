# data_preprocessing.py
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
from sklearn.model_selection import train_test_split

class DataProcessor:
    def preprocess_data(self, data):
        # Split the dataset into features and target variable
        X = data.drop('target', axis=1)
        y = data['target']
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        
        return X_train, X_test, y_train, y_test