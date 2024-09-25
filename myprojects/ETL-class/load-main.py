from extract import extract
# CSV to CSV
from load import load
dataset = extract.fromCSV(file_path="stocks.csv")
load.toCSV(file_path="stocks_load_copy1.csv",dataset=dataset)