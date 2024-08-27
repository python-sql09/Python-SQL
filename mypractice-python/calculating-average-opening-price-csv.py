# 19.4 Calculating the average opening price
import csv
with open('home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks_short.csv') as f:
    csv_file = csv.reader(f, delimiter=',')
    f.readline()
    sum = 0
    count = 0
    for row in csv_file:
        sum += float(row[1])
        count += 1
    print(sum/count)