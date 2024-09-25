from extract import extract
from load import load
e = extract()
dataset = e.fromCSV(file_path='/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/stocks1.csv', delimiter=',')
l = load()
l.toMONGODB(host="localhost", port=27017, username="testcsv", password="Vedha@369", db="testCSV", collection="cstocks", dataset=dataset)
