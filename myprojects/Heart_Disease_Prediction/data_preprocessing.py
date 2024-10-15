# data_preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score

class DataProcessor:
    def load_data(self, file_path):
        data = pd.read_csv(file_path)
        return data

    def preprocess_data(self, data):
        data = data.dropna()  # Handle missing values
        X = data.drop(columns=['target'])  # Adjust based on the actual target column
        y = data['target']
        return train_test_split(X, y, test_size=0.2, random_state=42)