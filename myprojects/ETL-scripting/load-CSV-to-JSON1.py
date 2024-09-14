import sys
import json

# Add the path to the custom 'extract' module
sys.path.append('/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting')

# Import the 'Extract' class
from extract import extract  # Make sure 'extract.py' contains the correct class name

class Load:
    # Method to save dataset to a JSON file
    def toJSON(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid JSON file path.")
        # Write the dataset to a JSON file
        with open(file_path, 'w') as jsonfile:
            json.dump(dataset, jsonfile, indent=4)  # Using indent for pretty formatting

# Initialize Extract and Load objects
e = extract()
# Load data from a CSV file
dataset = e.fromCSV(file_path='/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/stocks1.csv', delimiter=',')

# Initialize Load object and convert the dataset to a JSON file
l = Load()
l.toJSON(file_path='/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/stocks_copy.json', dataset=dataset)
