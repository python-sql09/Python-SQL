# Exercise 6: Self-­Assessment
import csv
import json

class Extract:
    def fromCSV(self, file_path, delimiter=",", quotechar="|"):
        """Reads data from a CSV file."""
        if not file_path:
            raise ValueError("You must provide a valid file path.")
        dataset = []
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as f:
                csv_file = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar)
                for row in csv_file:
                    dataset.append(row)
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        except IOError:
            raise IOError(f"Error opening CSV file: {file_path}")
        return dataset

    def fromJSON(self, file_path):
        """Reads data from a JSON file."""
        if not file_path:
            raise ValueError("You must provide a valid file path.")
        dataset = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as json_file:
                dataset = json.load(json_file)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON file: {file_path}")
        except IOError:
            raise IOError(f"Error opening JSON file: {file_path}")
        return dataset

def main():
    extractor = Extract()
    while True:
        try:
            # Prompt for CSV file path
            csv_path = input("Enter the path to the CSV file (or 'q' to quit): ")
            if csv_path.lower() == 'q':
                print("Exiting the program.")
                break
            dataset_csv = extractor.fromCSV(file_path=csv_path)
            print("CSV file loaded successfully.")
            print(dataset_csv)
            break
        except (ValueError, FileNotFoundError, IOError) as e:
            print(e)
            print("Please try again.")
    while True:
        try:
            # Prompt for JSON file path
            json_path = input("Enter the path to the JSON file (or 'q' to quit): ")
            if json_path.lower() == 'q':
                print("Exiting the program.")
                break
            dataset_json = extractor.fromJSON(file_path=json_path)
            print("JSON file loaded successfully.")
            print(dataset_json)
            break
        except (ValueError, FileNotFoundError, IOError) as e:
            print(e)
            print("Please try again.")

if __name__ == "__main__":
    main()