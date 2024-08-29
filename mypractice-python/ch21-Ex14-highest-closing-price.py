# Exercise 14: Highest Price at Closing
# Create a script that uses the filter() function to identify all records in the stocks.csv file
# where the highest price of the day is the close price.
import csv
# Function to read the CSV file into a list of dictionaries
def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
# Function to filter records where the highest price is equal to the closing price
def highest_price_at_closing(data):
    return filter(lambda row: float(row['High']) == float(row['Close']), data)
# Example usage
file_path = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks1.csv'  # Replace with the path to your CSV file
data = read_csv(file_path)
# Find and display records where the highest price is the same as the closing price
matching_days = list(highest_price_at_closing(data))
print("Records where the highest price of the day is the same as the closing price:")
for day in matching_days:
    print(f"Date: {day['Date']}, Open: {day['Open']}, High: {day['High']}, Low: {day['Low']}, Close: {day['Close']}")