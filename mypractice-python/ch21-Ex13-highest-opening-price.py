# Exercise 13: Highest Opening Price
# Create a script that uses the filter() function to identify all records in the stocks.csv file
# where the highest price of the day is the open price.
import csv
# Function to read the CSV file into a list of dictionaries
def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
# Function to filter records where the highest price is equal to the opening price
def highest_opening_price(data):
    return filter(lambda row: float(row['High']) == float(row['Open']), data)
# Example usage
file_path = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks1.csv'  # Replace with the path to your CSV file
data = read_csv(file_path)
# Find and display records where the highest price is the same as the opening price
matching_days = list(highest_opening_price(data))
print("Records where the highest price of the day is the same as the opening price:")
for day in matching_days:
    print(f"Date: {day['Date']}, Open: {day['Open']}, High: {day['High']}, Close: {day['Close']}")
    