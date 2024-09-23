from pymongo import MongoClient
from urllib.parse import quote_plus

# Encode the username and password
username = quote_plus("mongodb")
password = quote_plus("Deepa@369")

# Create a connection using the correctly encoded credentials
client = MongoClient(f"mongodb://{username}:{password}@localhost:27017/amazon_records")

# Access the database
db = client['amazon_records']

# Access the collection
collection = db['musical_instruments']

# Fetch documents from the collection
documents = collection.find({})

# Print each document
for doc in documents:
    print(doc)