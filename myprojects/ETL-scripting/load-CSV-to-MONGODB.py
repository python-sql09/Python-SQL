# 29 Using the toMONGODB method
import sys
sys.path.append('/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting')
from extract import extract  # Import your custom-built extract module
import pymongo

class Load:
    def toMONGODB(self, host, port, username, password, db, collection, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("You must input a valid database name.")
        if not collection:
            raise Exception("You must input a valid collection name.")
        
        # Connect to MongoDB
        client = pymongo.MongoClient(host=host, port=port, username=username, password=password)
        tmp_database = client[db]
        tmp_collection = tmp_database[collection]
        
        # Insert data into MongoDB collection
        tmp_collection.insert_many(dataset)

# Extract dataset from CSV and load to MongoDB
e = extract()
dataset = e.fromCSV(file_path='/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/stocks1.csv', delimiter=',')
l = Load()
l.toMONGODB(host="localhost", port=27017, username="testcsv", password="Vedha@369", db="testCSV", collection="cstocks", dataset=dataset)
