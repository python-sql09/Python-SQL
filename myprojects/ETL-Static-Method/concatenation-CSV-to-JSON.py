import csv
import json

# File paths
input_file = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/names.csv'
output_file = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/concatenate_data.json'

# List to store transformed records
transformed_data = []

# Step 1: Read the original CSV file
with open(input_file, mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Step 2: Iterate through each row
    for row in reader:
        # Concatenate first name and last name
        full_name = f"{row['first_name']} {row['last_name']}"
        
        # Create a new dictionary with full name and other remaining fields
        new_row = {'full_name': full_name}
        
        # Optionally, add other columns to the new row if needed
        for key, value in row.items():
            if key not in ['first_name', 'last_name']:
                new_row[key] = value
        
        # Add the new row to the transformed data
        transformed_data.append(new_row)

# Step 4: Write the transformed data to a JSON file
with open(output_file, mode='w') as jsonfile:
    json.dump(transformed_data, jsonfile, indent=4)

print(f"Transformed data has been saved to {output_file}.")