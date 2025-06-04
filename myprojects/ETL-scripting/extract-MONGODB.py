# --------------------------------------------------------------------------------------
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL
# Date        : September 09, 2024
# Description :  We will use the extract.py, fromMONGODB method as a model for extracting
# ----------------------------------------------------------------------------------------
import pymongo
class Extract:
    def fromMONGODB(self, host, port, username, password, db, collection, query=None, authSource="admin"):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, username, password, database, and collection name")

        try:
            client = pymongo.MongoClient(
                host=host,
                port=port,
                username=username,
                password=password,
                authSource=authSource
            )
            tmp_database = client[db]
            tmp_collection = tmp_database[collection]
            dataset = []
            if query:
                for document in tmp_collection.find(query):
                    dataset.append(document)
                return dataset
            for document in tmp_collection.find():
                dataset.append(document)
            return dataset
        except pymongo.errors.PyMongoError as e:
            print(f"Error: {e}")
            return None

# Example usage
e = Extract()
dataset = e.fromMONGODB(
    host="localhost",
    port=27017,
    username="admin",           # changed to your admin user
    password="admin@369",       # changed to your admin password
    db="amazon_records",
    collection="musical_instruments",
    authSource="admin"          # explicitly added authSource here
)
if dataset:
    print(len(dataset))
    print(dataset[0])
