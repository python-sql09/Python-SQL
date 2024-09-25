from extract import extract

# Create an instance of the extract class
e = extract()

# Call the method to extract data from MongoDB
dataset = e.fromMONGODB(
    host="localhost",
    port=27017,
    username="mongodb",
    password="Deepa@369",
    db="amazon_records",
    collection="musical_instruments",
    limit=10  # Specify the limit as an integer
)

if dataset:
    print(f"Number of documents retrieved: {len(dataset)}")
    print(dataset[0])
    print(dataset[1])


