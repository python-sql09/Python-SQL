# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/ETL-scripting
# Date        : March 27, 2025 to May 3, 2025
# Description : Using toJSON method load json file
# ----------------------------------------------------------------------------------------------------
import sys
import json
# Add the path to the custom 'extract' module
sys.path.append('ETL-scripting')
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
dataset = e.fromCSV(file_path = 'stocks1.csv', delimiter = ',')
l = load()
l.toJSON(file_path = "stocks_copy1.json", dataset = dataset)