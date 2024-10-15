# model_training.py
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

class ModelTrainer:
    def train_logistic_regression(self, X_train, y_train, X_test):
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = LogisticRegression()
        model.fit(X_train_scaled, y_train)
        return model.predict(X_test_scaled)

    def train_random_forest(self, X_train, y_train, X_test, scale_type="standard"):
        scaler = StandardScaler() if scale_type == "standard" else MinMaxScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train_scaled, y_train)
        return model.predict(X_test_scaled)

    def train_xgboost(self, X_train, y_train, X_test):
        scaler = MinMaxScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = XGBClassifier()
        model.fit(X_train_scaled, y_train)
        return model.predict(X_test_scaled)

    def train_svm(self, X_train, y_train, X_test):
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        # Define and fit the SVM model with class weights
        svm_model = SVC(class_weight='balanced')
        svm_model.fit(X_train_scaled, y_train)
        # Return the predictions
        return svm_model.predict(X_test_scaled)

    def train_knn(self, X_train, y_train, X_test, n_neighbors=5):
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = KNeighborsClassifier(n_neighbors=n_neighbors)
        model.fit(X_train_scaled, y_train)
        return model.predict(X_test_scaled)

    def train_naive_bayes(self, X_train, y_train, X_test):
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = GaussianNB()
        model.fit(X_train_scaled, y_train)
        return model.predict(X_test_scaled)