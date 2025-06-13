# ----------------------------------------------------------------------------------------------------
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com
# GitHub      : https://github.com/python-sql09/Python-SQL
# Date        : September 18, 2024
# Description : Load data from CSV into MongoDB (testCSV.cstocks)
# ----------------------------------------------------------------------------------------------------
import sys
import os
import pymongo

# Make sure the custom ETL extract module path is added
sys.path.append('/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting')

from extract import extract  # Import your custom-built extract module

class Load:
    def toMONGODB(self, host, port, username, password, db, collection, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("You must input a valid database name.")
        if not collection:
            raise Exception("You must input a valid collection name.")

        # Remove _id if exists to avoid duplication error
        for item in dataset:
            item.pop('_id', None)

        # Connect to MongoDB
        try:
            client = pymongo.MongoClient(
                host=host,
                port=port,
                username=username,
                password=password,
                authSource=db
            )
            tmp_database = client[db]
            tmp_collection = tmp_database[collection]

            # Insert data into MongoDB collection
            result = tmp_collection.insert_many(dataset, ordered=False)
            print(f"✅ Inserted {len(result.inserted_ids)} documents into '{db}.{collection}'")
        except pymongo.errors.BulkWriteError as bwe:
            print("⚠️ Some documents were not inserted due to duplication or write errors.")
            print(bwe.details)
        except Exception as e:
            print(f"❌ Error connecting or inserting to MongoDB: {str(e)}")
        finally:
            client.close()

# Extract dataset from CSV and load to MongoDB
if __name__ == "__main__":
    file_path = 'stocks1.csv'

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    e = extract()
    dataset = e.fromCSV(file_path=file_path, delimiter=',')

    print(f"📄 Total records loaded from CSV: {len(dataset)}")
    if dataset:
        print(f"🔍 Sample record: {dataset[0]}")

    l = Load()
    l.toMONGODB(
        host="localhost",
        port=27017,
        username="testcsv",
        password="Vedha@369",
        db="testCSV",
        collection="cstocks",
        dataset=dataset
    )


'''
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL
# Date        : September 12, 2024
# Description : Using toMONGODB method to load testCSV db
# ----------------------------------------------------------------------------------------------------
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
        client = pymongo.MongoClient(host=host, port=port, username=username, password=password, authSource=db)

        tmp_database = client[db]
        tmp_collection = tmp_database[collection]
        
        # Insert data into MongoDB collection
        tmp_collection.insert_many(dataset)

# Extract dataset from CSV and load to MongoDB
e = extract()
dataset = e.fromCSV(file_path='stocks1.csv', delimiter=',')
l = Load()
l.toMONGODB(host="localhost", port=27017, username="testcsv", password="Vedha@369", db="testCSV", collection="cstocks", dataset=dataset)
'''