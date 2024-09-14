import sys
sys.path.append('/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting')  # Add directory, not the file
from extract import extract

class transform:
    # Return the top N records from the dataset
    def head(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[:step]

    # Return the last N records from the dataset
    def tail(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[-step:]

# Initialize extract and connect to MongoDB
try:
    e = Extract()

    # Connect to MongoDB
    dataset = e.fromMONGODB(
        host="localhost", 
        port=27017, 
        username="mongodb", 
        password="Deepa@369", 
        db="amazon_records", 
        collection="musical_instruments"
    )

    # Ensure we have data
    if not dataset:
        raise Exception("The dataset is empty. Please check the MongoDB query or connection.")

    # Create transform object
    t = Transform()

    # Retrieve the top 5 records in the dataset
    dataset_1 = t.head(dataset=dataset, step=5)
    print("Top 5 records in the dataset:")
    for row in dataset_1:
        print(row['_id'])

    # Retrieve the bottom 5 records in the dataset
    dataset_2 = t.tail(dataset=dataset, step=5)
    print("\nBottom 5 records in the dataset:")
    for row in dataset_2:
        print(row['_id'])

except Exception as e:
    print(f"An error occurred: {e}")
