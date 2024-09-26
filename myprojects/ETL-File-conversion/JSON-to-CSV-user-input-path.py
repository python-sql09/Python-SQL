# Transforming JSON to CSV
# Write a Python program that prompts the user for the path of an existing JSON file and
# copies the data from that file into a new CSV file.
import json
import csv
import os

def json_to_csv(json_file_path, csv_file_path):
    """Converts JSON data into CSV format and writes it to a CSV file."""
    try:
        # Open the JSON file for reading
        with open(json_file_path, mode='r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)  # Load the JSON data
        
        # Check if the data is in a list of dictionaries format
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            print("Error: The JSON file does not contain a list of dictionaries.")
            return

        # Open the CSV file for writing
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            # Get the keys from the first dictionary to be used as the header
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()  # Write the header (fieldnames)
            writer.writerows(data)  # Write the rows (data)
            
        print(f"Data has been copied from '{json_file_path}' to '{csv_file_path}' successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{json_file_path}' or '{csv_file_path}'.")
    except json.JSONDecodeError:
        print("Error: Failed to parse the JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to prompt the user for JSON and CSV file paths."""
    json_file_path = input("Enter the path of the existing JSON file: ")
    csv_file_path = input("Enter the path for the new CSV file: ")
    
    if not os.path.isfile(json_file_path):
        print(f"Error: The file '{json_file_path}' does not exist.")
        return

    json_to_csv(json_file_path, csv_file_path)

if __name__ == "__main__":
    main()
