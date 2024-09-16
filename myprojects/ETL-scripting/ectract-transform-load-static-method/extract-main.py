'''# 2 Using the updated extract.py file
#import sys
#import csv
#sys.path.append('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/extract.py')
#sys.path.append('python-sql09/Python-SQL/mypractice-python/extract.py')
from extract import extract
dataset = extract.fromCSV(file_path = "/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks.csv")
print(dataset[0])
'''
import sys
import os

# Define the path to the directory where extract.py is located
extract_path = 'python-sql09/Python-SQL/myprojects/ETL-scripting/ectract-transform-load-static-method'
if os.path.exists(os.path.join(extract_path, 'extract.py')):
    sys.path.append(extract_path)
    from extract import extract
    # Assuming extract has a method called fromCSV
    dataset = extract.fromCSV(file_path="python-sql09/Python-SQL/myprojects/ETL-scripting/ectract-transform-load-static-method/stocks.csv")
    print(dataset[0])
else:
    print(f"extract.py not found in {extract_path}. Please check the file path.")
