# 18 Transforming the data with round_price
from extract import extract #import our custom built extract module
class transform:
     # check the dataset and input is empty 
   ''' def transform(self, dataset, attribute, new_attribute, transform_function, *args):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if not attribute or not new_attribute:
            raise Exception("The input attribute cannot be empty.")
        if not transform_function:
            raise Exception("The transform_function cannot be None.")
        new_dataset = list() #output of this function
        for row in dataset: #iterate through the input data
            t = transform_function(row[attribute], *args) #apply transformation function on column
            z = row.copy()
            z.update({new_attribute:t}) #create new column in the data
            new_dataset.append(z)
        return new_dataset'''
    def round_open_price(value, *args):
        return round(float(value))
e = extract()
dataset = e.fromCSV(file_path="/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/stocks1.csv")
print("Original dataset:")
print(dataset[0])

t = transform()
new_dataset = t.transform(dataset = dataset, attribute = "Open", 
new_attribute = "open_price_rounded", transform_function = round_open_price)
print("\nTransformed dataset:")
print(new_dataset[0])