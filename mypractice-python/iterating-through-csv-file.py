# 19.2 Iterating through a CSV file
import csv
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks_short.csv') as f:
    csv_file = csv.reader(f, delimiter=',')
    f.readline()
    # csv_file is an iterable object that we can iterate on using a for loop
    for row in csv_file:
        print(row) # print entire row