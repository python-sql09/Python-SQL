# --------------------------------------------------------------------------------------
# Project Name: Heart Disease Prediction
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      :https://github.com/python-sql09/Python-SQL/tree/main/myprojects/Heart_Disease_Prediction
# Date        :March 27, 2024 to May 3, 2024
# Description : This project applies data preprocessing, feature engineering, and multiple machine learning
#               algorithms to compare performance and identify the best predictive model.
# ----------------------------------------------------------------------------------------
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class ModelTrainer:
    def train_logistic_regression(self, X_train, y_train, X_test, max_iter=1000):
        """
        Train a Logistic Regression model.
        
        Parameters:
        X_train (array-like): Training features
        y_train (array-like): Training labels
        X_test (array-like): Test features
        max_iter (int): Maximum number of iterations for the solver

        Returns:
        array-like: Predictions for the test set
        """
        model = LogisticRegression(max_iter=300)
        model.fit(X_train, y_train)
        return model.predict(X_test)

    def train_random_forest(self, X_train, y_train, X_test, scale_type=None):
        """
        Train a Random Forest model.

        Parameters:
        X_train (array-like): Training features
        y_train (array-like): Training labels
        X_test (array-like): Test features
        scale_type (str): Type of scaling to apply ('standard' or 'minmax')

        Returns:
        array-like: Predictions for the test set
        """
        # Scale the data if specified
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
        """
        Train an XGBoost model.

        Parameters:
        X_train (array-like): Training features
        y_train (array-like): Training labels
        X_test (array-like): Test features

        Returns:
        array-like: Predictions for the test set
        """
        model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
        model.fit(X_train, y_train)
        return model.predict(X_test)

    def train_svm(self, X_train, y_train, X_test):
        """
        Train a Support Vector Machine model.

        Parameters:
        X_train (array-like): Training features
        y_train (array-like): Training labels
        X_test (array-like): Test features

        Returns:
        array-like: Predictions for the test set
        """
        model = SVC()
        model.fit(X_train, y_train)
        return model.predict(X_test)

    def train_knn(self, X_train, y_train, X_test):
        """
        Train a K-Nearest Neighbors model.

        Parameters:
        X_train (array-like): Training features
        y_train (array-like): Training labels
        X_test (array-like): Test features

        Returns:
        array-like: Predictions for the test set
        """
        model = KNeighborsClassifier()
        model.fit(X_train, y_train)
        return model.predict(X_test)

    def train_naive_bayes(self, X_train, y_train, X_test):
        """
        Train a Naive Bayes model.

        Parameters:
        X_train (array-like): Training features
        y_train (array-like): Training labels
        X_test (array-like): Test features

        Returns:
        array-like: Predictions for the test set
        """
        model = GaussianNB()
        model.fit(X_train, y_train)
        return model.predict(X_test)