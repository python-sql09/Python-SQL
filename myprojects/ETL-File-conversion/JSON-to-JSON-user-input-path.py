# Transforming JSON to JSON
# Write a Python program that prompts the user for the path of an existing JSON file and
# copies the data from that file into a new JSON file.
import json
import os

def json_to_json():
    # Prompt user for the source JSON file path
    source_file = input("Enter the path of the source JSON file: ")

    # Check if the source file exists
    if not os.path.exists(source_file):
        print("The file does not exist. Please check the file path.")
        return

    # Prompt user for the destination JSON file path
    destination_file = input("Enter the path where the new JSON file should be saved: ")

    try:
        # Open and read the source JSON file
        with open(source_file, 'r') as src:
            data = json.load(src)
        
        # Write the data into the new JSON file
        with open(destination_file, 'w') as dest:
            json.dump(data, dest, indent=4)

        print(f"Data successfully copied to {destination_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
json_to_json()