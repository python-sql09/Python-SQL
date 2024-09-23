# Extract data from deepadatabase.artists in MySQL, renaming one or more columns.
from extract import extract
from transform import transform
# open MYSQL database rename multiple column
# Fetch data from MySQL
e = extract()
query = "SELECT artistId, fname, lname, isHallOfFame FROM artist;"
dataset = e.fromMYSQL(
    host="localhost",
    username="root",
    password="Deepa@369",
    db="deeparecordshop",
    query=query
)
print("Original dataset:")
print(dataset)
print(len(dataset))
# Renaming columns using transform class
t = transform()
new_dataset = t.rename_attributes(
    dataset=dataset,
    attributes=["fname", "lname"],
    new_attributes=["first_name", "last_name"]
)
print("\nUpdated dataset:")
print(new_dataset)

