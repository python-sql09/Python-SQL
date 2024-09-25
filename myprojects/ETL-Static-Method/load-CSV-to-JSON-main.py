from extract import extract
from load import load
e = extract()
dataset = e.fromCSV(file_path = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/stocks1.csv', delimiter = ',')
l = load()
l.toJSON(file_path = "/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/stocks1_copy1.json", dataset = dataset)