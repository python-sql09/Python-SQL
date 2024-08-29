# Exercise 12: Bad Stock Market Day
# Create a script that uses the filter() function to identify all records in the stocks.csv file
# where the opening price is higher than the closing price.
import csv
# Function to read the CSV file into a list of dictionaries
def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
# Function to filter records where the opening price is higher than the closing price
def bad_stock_days(data):
    return filter(lambda row: float(row['Open']) > float(row['Close']), data)
# Example usage
file_path = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks1.csv'  # Replace with the path to your CSV file
data = read_csv(file_path)
# Find and display the bad stock market days
bad_days = list(bad_stock_days(data))
print("Records where the opening price is higher than the closing price:")
for day in bad_days:
    print(f"Date: {day['Date']}, Open: {day['Open']}, Close: {day['Close']}")