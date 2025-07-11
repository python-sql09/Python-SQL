# --------------------------------------------------------------------------------------
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/ETL-scripting
# Date        : September 09, 2024
# Description :  We will use the extract.py, fromSQLite method as a model for extracting
# ----------------------------------------------------------------------------------------
import sqlite3

class extract:
    def fromSQLite(self, db, query):
        if not db or not query:
            raise Exception("Please make sure that you input a valid database and query.")
        # Connect to the SQLite database
        connection = sqlite3.connect(db)
        # Set row factory to sqlite3.Row to get dictionary-like results
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        # Execute the query
        cursor.execute(query)
        # Fetch all results
        rows = cursor.fetchall()
        # Convert rows to list of dictionaries
        dataset = [dict(row) for row in rows]
        # Close cursor and connection
        cursor.close()
        connection.close()
        return dataset

# Example usage
e = extract()
query = "SELECT * FROM artist;"  # Adjust table name accordingly
dataset = e.fromSQLite(db="deeparecordshop.db", query=query)  # Specify the correct .db file
print(dataset)
print(len(dataset))