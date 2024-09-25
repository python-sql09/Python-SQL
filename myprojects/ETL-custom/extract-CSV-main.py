# 2 Using the updated extract.py file
from extract import extract
dataset = extract.fromCSV(file_path = "stocks.csv")
print(dataset[0])

