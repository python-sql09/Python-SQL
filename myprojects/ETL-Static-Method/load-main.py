from extract import extract
from load import load
dataset = extract.fromCSV(file_path="stocks.csv")
load.toCSV(file_path="stocks_load_copy.csv",dataset=dataset)