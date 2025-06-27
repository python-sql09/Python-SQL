class extract:
    @staticmethod
    def fromMONGODB(host, port, username, password, db, collection, query=None, limit=2):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, \
                            username, password, database, and collection name")
        import pymongo
        try:
            # URL-encode the username and password
            username = quote_plus(username)
            password = quote_plus(password)
            client = pymongo.MongoClient(
                f"mongodb://{username}:{password}@{host}:{port}/{db}?authSource=amazon_records"
            )
            tmp_database = client[db]
            tmp_collection = tmp_database[collection]
        
            dataset = list()
            if query:
                for document in tmp_collection.find(query).limit(limit):
                    dataset.append(document)
            else:
                for document in tmp_collection.find().limit(limit):
                    dataset.append(document)
        
            print(f"Number of documents retrieved: {len(dataset)}")
            return dataset
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return None
# In the main script:
username = quote_plus("mongodb")
password = quote_plus("Deepa@369")
e = extract()
dataset = e.fromMONGODB(host="localhost", port=27017, username="mongodb", password="Deepa@369", db="amazon_records", collection="musical_instruments", limit=2)
if dataset:
    print(f"Number of documents retrieved: {len(dataset)}")
    print(dataset[0])
    print(dataset[1])