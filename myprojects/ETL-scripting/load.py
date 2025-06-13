
# ----------------------------------------------------------------------------------------------------
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL
# Date        : September 18, 2024
# Description : ETL process is to load the transformed data into a relatively permanent storage location
# ----------------------------------------------------------------------------------------------------
from extract import extract
class load:
    # 22 Using the CSV method to Load
    def toCSV(self, file_path, dataset):
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

    def toJSON(self, file_path, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not file_path:
            raise Exception("You must provide a valid JSON file path.")
        import json
        with open(file_path, 'w') as jsonfile:
            json.dump(dataset, jsonfile, indent=4)  # Using indent for pretty formatting

    def toMYSQL(self, host, username, password, db, table, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("You must input a valid database name.")
        if not table:
            raise Exception("You must input a valid table name")
        import pymysql
        db = pymysql.connect(host = host, user=username, password = password, db = db,
                             cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        for row in dataset:
            placeholder = ", ".join(["%s"] * len(row))
            stmt = "insert into {table} ({columns}) values ({values});".format(table=table, 
                    columns=",".join(row.keys()), values = placeholder)
            cur.execute(stmt, list(row.values()))
        db.commit()
        cur.close()
        db.close()

    def toMONGODB(self, host, port, username, password, db, collection, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("You must input a valid database name.")
        if not collection:
            raise Exception("You must input a valid collection name.")
        import pymongo
        client = pymongo.MongoClient(
            host=host,
            port=port,
            username=username,
            password=password,
            authSource=db  # Specify authentication database explicitly
        )
        tmp_database = client[db]
        tmp_collection = tmp_database[collection]
        tmp_collection.insert_many(dataset)

if __name__ == "__main__":
    e = extract()
    dataset = e.fromCSV(file_path='stocks1.csv', delimiter=',')
    l = load()
    l.toMONGODB(
        host="localhost",
        port=27017,
        username="testcsv",
        password="Vedha@369",
        db="testCSV",
        collection="cstocks",
        dataset=dataset
)
