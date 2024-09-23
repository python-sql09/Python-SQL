# Exercise 5: Removing an Attribute CSV to CSV
# Write a Python program that performs the following tasks:
# •• Prompts the user for the path of an existing CSV file and an attribute in that file
# •• Reads the data from the file
# •• Removes the specified attribute
# •• Saves the transformed data to a new CSV file
import csv
import os

def remove_attribute_from_csv():
    # Prompt user for the source CSV file path
    source_file = input("Enter the path of the source CSV file: ")

    # Check if the source file exists
    if not os.path.exists(source_file):
        print("The file does not exist. Please check the file path.")
        return

    # Prompt user for the attribute (column name) to remove
    attribute_to_remove = input("Enter the name of the attribute (column) to remove: ")

    # Prompt user for the destination CSV file path
    destination_file = input("Enter the path where the new CSV file should be saved: ")

    try:
        # Read the CSV file
        with open(source_file, 'r') as src_file:
            reader = csv.DictReader(src_file)
            fieldnames = reader.fieldnames

            # Check if the attribute exists in the CSV file
            if attribute_to_remove not in fieldnames:
                print(f"The attribute '{attribute_to_remove}' does not exist in the file.")
                return

            # Remove the specified attribute from the fieldnames
            updated_fieldnames = [field for field in fieldnames if field != attribute_to_remove]

            # Write the transformed data to a new CSV file
            with open(destination_file, 'w', newline='') as dest_file:
                writer = csv.DictWriter(dest_file, fieldnames=updated_fieldnames)
                writer.writeheader()

                for row in reader:
                    del row[attribute_to_remove]
                    writer.writerow(row)

        print(f"The attribute '{attribute_to_remove}' has been removed and data saved to {destination_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
remove_attribute_from_csv()