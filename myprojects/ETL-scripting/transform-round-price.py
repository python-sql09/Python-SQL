# ---------------------------------------------------------------------------------------------------------
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL
# Date        : March 27, 2025 to May 3, 2025
# Description : The function, round_price is set up to round the given value to the nearest integer.
# -------------------------------------------------------------------------------------------------------
from extract import extract  # import our custom built extract module
class transform:
    def transform(self, dataset, attribute, new_attribute, transform_function):
        for row in dataset:
            row[new_attribute] = transform_function(row[attribute])
        return dataset

def round_open_price(value, *args):
    return round(float(value))

# --- Main script logic ---
e = extract()
dataset = e.fromCSV(file_path="stocks1.csv")

print("Original dataset:")
print(dataset[0])

t = transform()
new_dataset = t.transform(
    dataset=dataset,
    attribute="Open",
    new_attribute="open_price_rounded",
    transform_function=round_open_price
)

print("\nTransformed dataset:")
print(new_dataset[0])
'''
# ---------------------------------------------------------------------------------------------------------
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/
# Date        : September 15, 2024
# Description : We function, round_price, that is set up to round the given value to the nearest integer.
# -------------------------------------------------------------------------------------------------------
from extract import extract #import our custom built extract module
class transform:
    def round_open_price(value, *args):
        return round(float(value))
    e = extract()
    dataset = e.fromCSV(file_path="stocks1.csv")
    print("Original dataset:")
    print(dataset[0])

    t = transform()
    new_dataset = t.transform(dataset = dataset, attribute = "Open", 
    new_attribute = "open_price_rounded", transform_function = round_open_price)
    print("\nTransformed dataset:")
    print(new_dataset[0])
'''