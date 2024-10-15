# Load and preprocess data
data = load_data("data/diabetes_data.csv")
X, y = preprocess_data(data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate models

# Logistic Regression
logistic_preds = train_logistic_regression(X_train, y_train, X_test)
print("Logistic Regression:")
evaluate_model(y_test, logistic_preds)

# Random Forest
rf_preds = train_random_forest(X_train, y_train, X_test)
print("\nRandom Forest:")
evaluate_model(y_test, rf_preds)

# K-Nearest Neighbors
knn_preds = train_knn(X_train, y_train, X_test)
print("\nK-Nearest Neighbors:")
evaluate_model(y_test, knn_preds)

# XGBoost
xgb_preds = train_xgboost(X_train, y_train, X_test)
print("\nXGBoost:")
evaluate_model(y_test, xgb_preds)