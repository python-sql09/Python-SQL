# Removing Duplicates
# Write a Python program that reads a data file, identifies duplicate records in the data file,
# removes duplicates, and saves the new dataset in a new file.
import csv

# File paths
input_file = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/bank_trans.csv'
output_file = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/cleaned_bank_trans.csv'

# Set to track unique records
unique_records = set()

# Step 1: Read the CSV file and identify duplicates
with open(input_file, mode='r') as csvfile:
    reader = csv.reader(csvfile)
    
    # Step 2: Open the output file to write non-duplicate records
    with open(output_file, mode='w', newline='') as newfile:
        writer = csv.writer(newfile)
        
        # Iterate over each row
        for row in reader:
            row_tuple = tuple(row)  # Convert row to a tuple to make it hashable
            if row_tuple not in unique_records:
                # Step 3: Add the unique row to the set and write to the new file
                unique_records.add(row_tuple)
                writer.writerow(row)

print(f"Duplicates removed. Cleaned data saved to {output_file}.")