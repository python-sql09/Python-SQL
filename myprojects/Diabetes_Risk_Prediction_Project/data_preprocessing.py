# data_preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def load_data(file_path):
    data = pd.read_csv(file_path)
    print("✅ Data Loaded Successfully")
    print("Shape:", data.shape)
    print("Columns:", data.columns.tolist())
    print("First 5 rows:\n", data.head())
    return data


def preprocess_data(data):
    # Handling missing values
    data = data.fillna(data.mean())

    # Separate features and target
    X = data.drop(columns=['Outcome'])  # Target column is Outcome
    y = data['Outcome']

    print("\n✅ Preprocessing Done")
    print("Features shape:", X.shape)
    print("Target distribution:\n", y.value_counts())

    return X, y


if __name__ == "__main__":
    # Load and preprocess data
    data = load_data("diabetes_risk_prediction_extended.csv")
    X, y = preprocess_data(data)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("\n✅ Train-Test Split Done")
    print("Train size:", X_train.shape, " Test size:", X_test.shape)