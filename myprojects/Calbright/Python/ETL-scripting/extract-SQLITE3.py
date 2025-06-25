# 4 The fromMySQL method in the extract class
import sqlite3
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
print(len(dataset))
