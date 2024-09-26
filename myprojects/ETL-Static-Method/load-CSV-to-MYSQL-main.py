from extract import extract
from load import load
e = extract()
dataset = e.fromCSV(file_path='/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/stocks.csv', delimiter=',')
l = load()
l.toMYSQL(host="localhost", username="root", password="Deepa@369", db="test", table="stocks", dataset=dataset)