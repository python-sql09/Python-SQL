# 7 The current status of the extract class
# 7 Alltogether CSV, JSON, MySQL, MongoDB
class extract:
    def fromCSV(self, file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter = delimiter,quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset

    def fromJSON(self, file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

     # extract data from Mysql DataBase
    # 4 The fromMySQL method in the extract class   
    import pymysql    
    def fromMYSQL(self, host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, username, password, database, and query.")       
        # Connect to the MySQL database
        connection = pymysql.connect(
            host=host,
            user=username,
            password=password,
            database=db,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            # Create a cursor object
            with connection.cursor() as cursor:
                # Execute the query
                cursor.execute(query)
                # Fetch all the results
                dataset = cursor.fetchall()
        finally:
            # Close the connection
            connection.close()
        return dataset

    # extract data from Mongo DataBase
    import pymongo
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

