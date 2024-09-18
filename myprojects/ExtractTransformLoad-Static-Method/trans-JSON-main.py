# Extract data from data.json, removing one or more columns.
from extract import extract
from transform import transform
e = extract()
dataset = e.fromJSON(file_path = "movies.json")
print("Original dataset:")
print(dataset[0])
print(dataset)
t = transform()
new_dataset = t.remove_attributes(dataset = dataset, attributes = ["runtime","year"])
print("\nTransformed dataset:")
print(new_dataset[0])