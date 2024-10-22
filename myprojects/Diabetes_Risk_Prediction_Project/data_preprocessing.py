#data_preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Example usage in main script
data = load_data("/home/deepa3/python-sql09/Python-SQL/myprojects/Diabetes_Risk_Prediction_Project/diabetes_risk_prediction_extended.csv")

def preprocess_data(data):
    # Handling missing values
    data = data.fillna(data.mean())
    
    # Separate features and target
    X = data.drop(columns=['Outcome'])  # Adjust based on actual target column name
    y = data['Outcome']
    
    return X, y

X, y = preprocess_data(data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)