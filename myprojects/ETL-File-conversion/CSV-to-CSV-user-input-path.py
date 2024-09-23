# Exercise 1: Transforming CSV to CSV
# Write a Python program that prompts the user for the path of an existing CSV file and 
# copies the data from that file into a new CSV file.
import csv
import os

def copy_csv(input_path, output_path):
    """Copies data from the input CSV file to the output CSV file."""
    try:
        with open(input_path, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                for row in reader:
                    writer.writerow(row)
        print(f"Data has been copied from '{input_path}' to '{output_path}' successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{input_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{input_path}' or '{output_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to prompt user for file paths and copy the CSV data."""
    input_path = input("Enter the path of the existing CSV file: ")
    output_path = input("Enter the path for the new CSV file: ")
    
    if not os.path.isfile(input_path):
        print(f"Error: The file '{input_path}' does not exist.")
        return

    copy_csv(input_path, output_path)

if __name__ == "__main__":
    main()