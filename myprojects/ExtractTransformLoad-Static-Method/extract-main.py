# 2 Using the updated extract.py file
#import sys
#import csv
#sys.path.append('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/extract.py')
#sys.path.append('python-sql09/Python-SQL/mypractice-python/extract.py')
from extract import extract
dataset = extract.fromCSV(file_path = "stocks.csv")
print(dataset[0])

