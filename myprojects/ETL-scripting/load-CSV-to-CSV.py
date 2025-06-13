# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL
# Date        : September 18, 2024
# Description : Using toCSV method load csv file
# ----------------------------------------------------------------------------------------------------
from extract import extract
class load:
    def toCSV(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid CSV file path.")
        import csv
        with open(file_path, 'w') as csvfile:
            fieldnames = dataset[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(dataset)
e = extract()
dataset = e.fromCSV(file_path = 'stocks1.csv',delimiter = ',')
l = load()
l.toCSV(file_path = "stocks1_copy.csv", dataset = dataset)