# data_preprocessing.py
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