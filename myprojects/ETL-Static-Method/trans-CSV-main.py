# 4 Testing the new transform.py file
from extract import extract
from transform import transform

# round price display CSV
def round_open_price(value,*args):
    return round(float(value))
dataset = extract.fromCSV(file_path = "stocks.csv")
print(dataset[0])
new_dataset = transform.transform(dataset = dataset, attribute = "Open",
new_attribute = "open_price_rounded",
transform_function = round_open_price)
print(new_dataset[0])

# open CSV file and Rename multiple column 
'''
e = extract()
dataset = e.fromCSV(file_path="stocks1.csv")
print("Original dataset:")
print(dataset[0])
t = transform()
new_dataset = t.rename_attributes(dataset = dataset, attributes = ["Open","Close"],
new_attributes = ["open_price", "close_price"])
print("\nUpdated dataset:")
print(new_dataset[0])
'''

