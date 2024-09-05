# 4 The fromMySQL method in the extract class
'''import sqlite3
class extract:
    def fromSQLite(self, db, query):
        if not db or not query:
            raise Exception("Please make sure that you input a valid database and query.")
        
        # Connect to the SQLite database
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch all results
        dataset = cursor.fetchall()
        
        # Close cursor and connection
        cursor.close()
        connection.close()
        
        return dataset

# Example usage
e = extract()
query = "SELECT * FROM artist;"  # Adjust table name accordingly
dataset = e.fromSQLite(db="deeparecordshop.db", query=query)  # Specify the correct .db file
print(dataset)
print(len(dataset))'''

import mysql.connector
from mysql.connector import Error

class extract:
    def fromMYSQL(self, host, username, password, db, query):
        if not host or not username or not password or not db or not query:
            raise Exception("Please make sure that you input a valid host, username, password, database, and query.")
        
        try:
            # Connect to the MySQL database
            connection = mysql.connector.connect(
                host=host,
                user=username,
                password=password,
                database=db
            )
            if connection.is_connected():
                print("Connected to MySQL database")

                cursor = connection.cursor(dictionary=True)
                
                # Execute the query
                cursor.execute(query)
                
                # Fetch all results
                dataset = cursor.fetchall()
                
                # Close cursor and connection
                cursor.close()
                connection.close()
                
                return dataset
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

# Example usage
e = extract()
query = "SELECT * FROM artist;"  # Adjust the table name to match your MySQL schema
dataset = e.fromMYSQL(host="localhost", username="root", password="admin", db="deeparecordshop", query=query)
print(dataset)
print(len(dataset))
