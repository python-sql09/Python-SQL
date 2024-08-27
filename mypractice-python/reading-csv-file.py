# 19.1 Reading a CSV file
#•• Date: The date of the following data
#•• Open: The opening price on that date
#•• High: The highest price on that date
#•• Low: The lowest price on that date
#•• Close: The closing price on that date
#•• Volume: The number of shares traded on that date
import csv
# Use open function to read the CSV file and create
# a file object f:
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks_short.csv') as f:
    # Use the reader class under the csv module to
    # read the file using comma as the delimiter
    csv_file = csv.reader(f, delimiter=',')
    row = f.readline() # Read the firstline of the .csv
    print(row)
    row = f.readline() # Read the firstline of the .csv
    print(row)