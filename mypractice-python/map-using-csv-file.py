# 21.10 Using map on a CSV file
def fromCSV(path,delimiter,quotechar):
    import csv # import the csv module
    data=list() # convert the CSV data into a list
    with open(path, newline='') as csvfile: # open the file
        filecontent = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar)
        # access the content of the file
        for row in filecontent: # iterate through the rows
            data.append(row)
    # save each row as a dictionary
    # item in the data list
    return data
def extract_month(row):
    # input is the entire row of data
    # extract the month from the date field
    # add the month field to the row and return the row
    value = row['Date']
    MM=""
    # split function in python used to divide strings based on some delimiter
    a = value.split("/")
    MM = a[0]
    #implement logic here
    new_row = row.copy()
    new_row.update({'Month':MM})
    return new_row
data=fromCSV(path='/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks1.csv',delimiter=',',quotechar='|')
print(data[0])
data_mapped = map(extract_month,data)
data_mapped_list = list(data_mapped)
print(data_mapped_list[0])