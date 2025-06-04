# ---------------------------------------------------------------------------------------------------------
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL
# Date        : September 12, 2024
# Description : We start by importing the extract class in extract.py. We then create separate head and
#               tail functions to retrieve a user-specified number of records from the dataset.
# -------------------------------------------------------------------------------------------------------
import sys
sys.path.append('ETL-scripting')  # Add directory, not the file
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
    e = extract()
    # Connect to MongoDB
    dataset = e.fromMONGODB(
        host="localhost", 
        port=27017, 
        username="admin",
        password="admin@369",
        db="amazon_records", 
        collection="musical_instruments",
        #authSource = "admin"  # explicitly added authSource here
    )
    # Ensure we have data
    if not dataset:
        raise Exception("The dataset is empty. Please check the MongoDB query or connection.")

    # Create transform object
    t = transform()

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
