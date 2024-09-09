# 13 Removing items in the transform class
from extract import extract #import our custom built extract module
class transform:
    def remove_attribute(self, dataset, attribute):
        new_dataset = list()
        for row in dataset:
            new_row = row
            if attribute in new_row.keys():
                del new_row[attribute]
                new_dataset.append(new_row)
        return new_dataset
e = extract()
dataset = e.fromCSV(file_path = "/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/stocks1.csv")
print("Original dataset:")
print(dataset[0])
t = transform()
new_dataset = t.remove_attribute(dataset = dataset, attribute = "Open")
print("\nTransformed dataset:")
print(new_dataset[0])