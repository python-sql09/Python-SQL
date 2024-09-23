# Exercise 7: Confirming an Attribute
# Write a Python program that performs the following tasks:
# •• Prompts the user for the path of an existing file of any data type
# •• Prompts the user for the name of an attribute
# •• Checks whether or not the named attribute exists in the data source
# •• Prints a user-­friendly response to inform the user whether the attribute exists in
# the data source
import csv
import json
import os

def confirm_attribute():
    # Prompt for file path
    file_path = input("Enter the path of the file (CSV or JSON): ")
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return
    # Prompt for attribute name
    attribute_name = input("Enter the name of the attribute: ")
    # Check if the file is CSV or JSON based on its extension
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.csv':
        # Handle CSV file
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            # Check if the attribute exists in the CSV header
            if attribute_name in reader.fieldnames:
                print(f"Attribute '{attribute_name}' exists in the CSV file.")
            else:
                print(f"Attribute '{attribute_name}' does NOT exist in the CSV file.")
    elif file_extension == '.json':
        # Handle JSON file
        with open(file_path, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            # Check if the attribute exists in any dictionary inside the JSON file
            if isinstance(data, list):
                if any(attribute_name in item for item in data if isinstance(item, dict)):
                    print(f"Attribute '{attribute_name}' exists in the JSON file.")
                else:
                    print(f"Attribute '{attribute_name}' does NOT exist in the JSON file.")
            elif isinstance(data, dict):
                if attribute_name in data:
                    print(f"Attribute '{attribute_name}' exists in the JSON file.")
                else:
                    print(f"Attribute '{attribute_name}' does NOT exist in the JSON file.")
            else:
                print("Error: The JSON file structure is not supported.")
    else:
        print("Error: Unsupported file type. Only CSV and JSON files are allowed.")
# Call the function
confirm_attribute()

#Result
# First Input enter full path like below
# Second Input is header in the file
'''
linuxdeepa@linux-eh70:~/python-sql09/Python-SQL/myprojects/ETL-File-conversion> python3 conforming-attribute.py
Enter the path of the file (CSV or JSON): /home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-File-conversion/stocks.csv
Enter the name of the attribute: Date
Attribute 'Date' exists in the CSV file.
'''