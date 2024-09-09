# 6 Adding the fromMONGODB method
 # extract data from Mongo DataBase
import pymongo

class Extract:
    def fromMONGODB(self, host, port, username, password, db, collection, query=None):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, username, password, database, and collection name")

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
            dataset = list()
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
dataset = e.fromMONGODB(host="localhost", port=27017, username="mongodb", password="Deepa@369", db="amazon_records", collection="musical_instruments")
if dataset:
    print(len(dataset))
    print(dataset[0])
