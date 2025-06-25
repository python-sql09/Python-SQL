# Guide: Reading a CSV file with pandas
import pandas as pd

# Step 1: Load a CSV file
df = pd.read_csv('data.csv')  # Ensure 'data.csv' is in your directory

# Step 2: View the first few rows
print(df.head())

# Step 3: Check for missing values
print(df.isnull().sum())
