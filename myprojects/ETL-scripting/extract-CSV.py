# We will use the extract.py fromCSV method as a model for extracting
# data from other types of sources.
# 2 extract.py: The extract class shell
class extract:
    # 2 Creating the fromCSV method
    def fromCSV(self, file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter = delimiter, quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset
   
e = extract()
dataset = e.fromCSV(file_path="/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/got_chars.csv")
for row in dataset:
    print(row)
print(len(dataset))