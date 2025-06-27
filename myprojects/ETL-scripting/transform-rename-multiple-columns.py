# ---------------------------------------------------------------------------------------------------------
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL
# Date        : March 27, 2025 to May 3, 2025
# Description : One common transformation step is to rename one or more attributes for extracted data.
# -------------------------------------------------------------------------------------------------------
from extract import extract #import our custom built extract module
class transform:
    #rename multiple columns from the dataset
    def rename_attributes(self,dataset,attributes,new_attributes):
        if not attributes or not new_attributes:
            raise Exception("The attributes cannot be empty.")
        if len(attributes) != len(new_attributes):
            raise Exception("The number of new column names must match the number of \
existing column names.")
        new_dataset = list()
        for row in dataset:
            new_row = row
            for i in range(0,len(attributes)):
                attribute = attributes[i]
                new_attribute = new_attributes[i]
                if attribute in new_row.keys():
                    val = row[attribute]
                    del new_row[attribute]
                    new_row[new_attribute] = val
                else:
                    raise Exception("Operation is not possible because the key " + \
str(key)+ \
" does not exist in one of the rows in the dataset.")
            new_dataset.append(new_row)
        return new_dataset
e = extract()
dataset = e.fromCSV(file_path="stocks1.csv")
print("Original dataset:")
print(dataset[0])
t = transform()
new_dataset = t.rename_attributes(dataset = dataset, attributes = ["Open","Close"],
new_attributes = ["open_price", "close_price"])
print("\nUpdated dataset:")
print(new_dataset[0])
    