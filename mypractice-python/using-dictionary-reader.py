# 19.6 Using a DictReader
import csv
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks.csv') as f:
    csv_file = csv.DictReader(f, delimiter=',')
    vol = None
    max_vol = None
    for row in csv_file:
        vol = int(row["Volume"])
        if max_vol == None or max_vol < vol:
            max_vol = vol
    print(max_vol)