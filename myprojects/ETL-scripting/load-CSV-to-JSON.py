# 24 Using the JSON file to load csv to json)
import sys
import json

# Add the path to the custom 'extract' module
sys.path.append('/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting')
from extract import extract
class load:
    def toJSON(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid JSON file path.")
        import csv
        with open(file_path, 'w') as jsonfile:
            json.dump(dataset, jsonfile, indent=4)  # Using indent for pretty formatting
e = extract()
dataset = e.fromCSV(file_path = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/stocks1.csv', delimiter = ',')
l = load()
l.toJSON(file_path = "/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/stocks_copy1.json", dataset = dataset)