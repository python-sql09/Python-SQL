# 4 The fromMySQL method in the extract class
import pymysql

class Extract:
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

# Example usage
e = Extract()
query = "SELECT * FROM artist;"
dataset = e.fromMYSQL(
    host="localhost",
    username="root",
    password="Deepa@369",
    db="deeparecordshop",
    query=query
)

print(dataset)
print(len(dataset))