# --------------------------------------------------------------------------------------
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL
# Date        : September 06, 2024
# Description :  We will use the extract.py fromCSV method as a model for extracting
# ----------------------------------------------------------------------------------------
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
dataset = e.fromCSV(file_path="got_chars.csv")
for row in dataset:
    print(row)
print(len(dataset))