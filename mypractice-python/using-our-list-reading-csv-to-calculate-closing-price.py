# 19.8 Using our list from reading a CSV file to calculate the closing price
def read_csv(filepath,delimiter=","):
    import csv
    dataset = list()
    with open(filepath) as f:
        csv_file = csv.DictReader(f, delimiter=delimiter)
        for row in csv_file:
            dataset.append(row)
    return dataset
dataset = read_csv("/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/stocks.csv")
total = 0
for row in dataset:
    total += float(row["Close"])
    print("Close: " + str(row["Close"]))
    print("------")
    print(total)