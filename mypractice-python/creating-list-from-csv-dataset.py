# 19.7 Creating a list from our dataset
def read_csv(filepath,delimiter=","):
    import csv
    dataset = list()
    with open(filepath) as f:
        # use the DictReader function of the csv module to
        # read the file using the same delimiter
        csv_file = csv.DictReader(f, delimiter=delimiter)
        # csv_file is an iterable object that we can iterate on using a for loop
        for row in csv_file:
            dataset.append(row)
    return dataset
dataset = read_csv("/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks_short.csv")
print(len(dataset)) # number of rows in the dataset
print("------")
print(dataset[0])
# print first row in the dataset
print("------")
print(dataset)