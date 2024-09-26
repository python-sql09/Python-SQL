# Renaming an Attribute CSV to CSV
# Write a Python program that performs the following tasks:
#  •• Prompts the user for the path of an existing CSV file, an attribute in that file, and a
#  new name for the same attribute
#  •• Reads the data from the file
#  •• Renames the specified attribute
#  •• Saves the transformed data to a new CSV file
import csv
import os

def rename_attribute_in_csv():
    # Prompt user for the source CSV file path
    source_file = input("Enter the path of the source CSV file: ")

    # Check if the source file exists
    if not os.path.exists(source_file):
        print("The file does not exist. Please check the file path.")
        return

    # Prompt user for the attribute (column name) to rename
    attribute_to_rename = input("Enter the name of the attribute (column) to rename: ")

    # Prompt user for the new name of the attribute
    new_attribute_name = input("Enter the new name for the attribute: ")

    # Prompt user for the destination CSV file path
    destination_file = input("Enter the path where the new CSV file should be saved: ")

    try:
        # Read the CSV file
        with open(source_file, 'r') as src_file:
            reader = csv.DictReader(src_file)
            fieldnames = reader.fieldnames

            # Check if the attribute exists in the CSV file
            if attribute_to_rename not in fieldnames:
                print(f"The attribute '{attribute_to_rename}' does not exist in the file.")
                return

            # Rename the specified attribute in the fieldnames
            updated_fieldnames = [new_attribute_name if field == attribute_to_rename else field for field in fieldnames]

            # Write the transformed data to a new CSV file
            with open(destination_file, 'w', newline='') as dest_file:
                writer = csv.DictWriter(dest_file, fieldnames=updated_fieldnames)
                writer.writeheader()

                for row in reader:
                    # Update the row to rename the attribute key
                    row[new_attribute_name] = row.pop(attribute_to_rename)
                    writer.writerow(row)

        print(f"The attribute '{attribute_to_rename}' has been renamed to '{new_attribute_name}' and data saved to {destination_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
rename_attribute_in_csv()