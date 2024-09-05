# 6 Adding the fromMONGODB method
class extract:
    def fromMONGODB(self, host, port, username, password, db, collection, query = None):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, username, \
password, database, and collection name")
        import pymongo
        client = pymongo.MongoClient(host = host, port = port,username = username,
password = password)
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
e = extract()
#update the values here based on your own mongodb options if necessary
dataset = e.fromMONGODB(host = "localhost", port = 27017, username = "admin",
password = "admin", db = "amazon_reviews",
collection = "musical_instruments")
print(len(dataset))
print(dataset[0])      