# 22 Using the CSV file to load (csv to csv)
import sys
sys.path.append('/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting')  # Adjust the path as necessary
from extract import extract  # Import the Extract class
class Load:
    def toCSV(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid CSV file path.")
        import csv
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = dataset[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dataset)
# Initialize Extract and load data
e = extract()
dataset = e.fromCSV(file_path='/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/stocks1.csv', delimiter=',')
# Initialize Load and save data to CSV
l = Load()
l.toCSV(file_path="/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/stocks1.copy1.csv", dataset=dataset)