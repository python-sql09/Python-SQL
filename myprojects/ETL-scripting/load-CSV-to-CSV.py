# 22 Using the CSV file to load (csv to csv)
class load:
    def toCSV(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid CSV file path.")
        import csv
        with open(file_path, 'w') as csvfile:
            fieldnames = dataset[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(dataset)
e = extract()
dataset = e.fromCSV(file_path = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/stocks1.csv',delimiter = ',')
l = load()
l.toCSV(file_path = "/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/stocks1_copy.csv", dataset = dataset)