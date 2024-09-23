# 9 Additional exception handling in the load class
from extract import extract
class load:
    @staticmethod
    def toCSV(file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid CSV file path.")
        import csv
        with open(file_path, 'w') as csvfile:
            fieldnames = dataset[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(dataset)

    @staticmethod
    def toJSON(file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid JSON file path.")
        import json
        with open(file_path, 'w') as jsonfile:
            json.dump(dataset, jsonfile)

    @staticmethod
    def toMYSQL(host, username, password, db, table, dataset):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, username, \
                                password, database, and query.")
        try:
            import pymysql
            Pythondb = pymysql.connect(host = host, user = username, password = password,
                                        db = db, cursorclass = pymysql.cursors.DictCursor)
            cur = db.cursor()
            cur.execute(query)
            dataset = list()
            for r in cur:
                dataset.append(r)
            db.commit()
            cur.close()
            db.close()
            return dataset
        except pymysql.InternalError as error:
            print(error)
            raise Exception("Error while reading data from MySQL.")

    @staticmethod
    def toMONGODB(host, port, username, password, db, collection, dataset):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, username, \
                                password, database, and collection name")
        try:
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
        except pymongo.errors.PyMongoError as e:
            print(e)
            raise Exception("Error while reading data from MongoDB.")