
# Usage
from extract import extract
from transform import transform
#format the output nicely
#from pprint import pprint

# Create an instance of Extract
e = extract()

# Connect to MongoDB and fetch data
dataset = e.fromMONGODB(
    host="localhost", 
    port=27017, 
    username="mongodb", 
    password="Deepa@369", 
    db="amazon_records", 
    collection="musical_instruments",
    limit=10  # Specify the limit here
)

# Assuming transform is correctly implemented
t = transform()

# Print the top 10 records in the dataset
if dataset:
    print("Top 10 records in the dataset:")
    #format the output nicely
    #for row in dataset:
    #    pprint(row)
    for row in dataset:
        # This will print the Id only
        print(row['_id'])
        # This will print the entire document
        # print(row) 
else:
    print("No data retrieved.")