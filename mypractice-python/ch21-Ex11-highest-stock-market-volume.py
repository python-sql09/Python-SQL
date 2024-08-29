# Exercise 11: Highest Stock Market Volume
# Create a script that uses the reduce() function to compute the trading day where the
# highest volume was recorded in the stocks.csv file. You can use any functions that are
# appropriate for the task, but you must include the reduce() function at least once.
# Display the results in a user-­friendly format.
import csv
from functools import reduce
# Function to read the CSV file into a list of dictionaries
def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
# Function to find the trading day with the highest trading volume using reduce
def highest_volume_day(data):
    return reduce(lambda max_row, current_row: max_row if int(max_row['Volume']) > int(current_row['Volume']) else current_row, data)
# Example usage
file_path = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks1.csv'  # Replace with the path to your CSV file
data = read_csv(file_path)
# Find the trading day with the highest trading volume
highest_volume = highest_volume_day(data)
# Display the result in a user-friendly format
print("Trading day with the highest trading volume:")
print(f"Date: {highest_volume['Date']}")
print(f"Volume: {highest_volume['Volume']}")
print(f"Open: {highest_volume['Open']}")
print(f"High: {highest_volume['High']}")
print(f"Low: {highest_volume['Low']}")
print(f"Close: {highest_volume['Close']}")