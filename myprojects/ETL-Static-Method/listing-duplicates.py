# Listing Duplicates
# Write a Python program that reads a data file, identifies duplicate records in the data file,
# and prints a list of the duplicate records.
import csv
from collections import defaultdict

# File to read
input_file = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/bank_trans.csv'

# Dictionary to track the occurrences of records
record_tracker = defaultdict(int)
duplicate_records = []

# Step 1: Read the CSV file
with open(input_file, mode='r') as csvfile:
    reader = csv.reader(csvfile)
    
    # Step 2: Identify duplicates by counting occurrences of each record
    for row in reader:
        row_tuple = tuple(row)  # Convert the row to a tuple (lists cannot be dictionary keys)
        record_tracker[row_tuple] += 1  # Increment the count of this record
        
        # Step 3: If a record appears more than once, add it to the duplicates list
        if record_tracker[row_tuple] == 2:  # Only consider it a duplicate the first time it's repeated
            duplicate_records.append(row_tuple)

# Step 4: Print the list of duplicate records
if duplicate_records:
    print("Duplicate Records:")
    for record in duplicate_records:
        print(record)
else:
    print("No duplicate records found.")