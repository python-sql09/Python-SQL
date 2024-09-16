# 18 Transforming the data with round_price
from extract import extract #import our custom built extract module
class transform:
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