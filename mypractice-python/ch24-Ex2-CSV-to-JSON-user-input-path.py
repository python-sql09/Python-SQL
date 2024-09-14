# Exercise 2: Transforming CSV to JSON
# Write a Python program that prompts the user for the path of an existing CSV file and 
# copies the data from that file into a new JSON file.
import csv
import json
import os

def csv_to_json(csv_file_path, json_file_path):
    """Converts CSV data into JSON format and writes it to a JSON file."""
    try:
        # Open the CSV file for reading
        with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)  # Read the CSV file as a dictionary
            data = [row for row in reader]  # Convert the CSV data to a list of dictionaries
            
        # Open the JSON file for writing and dump the data
        with open(json_file_path, mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)  # Write the JSON data with indentation for readability
            
        print(f"Data has been copied from '{csv_file_path}' to '{json_file_path}' successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{csv_file_path}' or '{json_file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to prompt the user for CSV and JSON file paths."""
    csv_file_path = input("Enter the path of the existing CSV file: ")
    json_file_path = input("Enter the path for the new JSON file: ")
    
    if not os.path.isfile(csv_file_path):
        print(f"Error: The file '{csv_file_path}' does not exist.")
        return

    csv_to_json(csv_file_path, json_file_path)

if __name__ == "__main__":
    main()