# 19.3 Iterating through a CSV file and printing individual items
import csv
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks_short.csv') as f:
    csv_file = csv.reader(f, delimiter=',')
    for row in csv_file:
        print(row[0], " -­", row[1] )