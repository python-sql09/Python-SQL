# Date Validity
# Write a Python program that extracts data from a data file containing a date (such as
# stocks.csv) and checks that all rows include valid dates. The program should display a val-
# idation warning message if there are any rows that contain invalid dates or an appropriate
# user-­friendly message if all dates are valid.
import csv
from datetime import datetime

# Step 1: Read the original CSV file and extract the date
input_file = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/stocks2.csv'
output_file = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/stocks_with_weekday1.csv'

# Open the input CSV file
with open(input_file, mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Step 2: Prepare to write to the new CSV file
    fieldnames = reader.fieldnames + ['Day_of_Week']  # Adding the new column
    
    with open(output_file, mode='w', newline='') as newfile:
        writer = csv.DictWriter(newfile, fieldnames=fieldnames)
        writer.writeheader()  # Write header with the new column
        
        # Step 3: Iterate over each row, transform the date to day of week
        for row in reader:
            date_str = row['Date']  # Assuming the date is in a 'Date' column
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')  # Convert string to date object
            day_of_week = date_obj.strftime('%A')  # Get day of the week (e.g., Monday, Tuesday)
            
            # Add the day of week to the row
            row['Day_of_Week'] = day_of_week
            
            # Step 4: Write the transformed row to the new file
            writer.writerow(row)

print(f"Data has been successfully written to {output_file}")