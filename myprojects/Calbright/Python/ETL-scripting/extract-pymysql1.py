import pymysql

class Extract:
    def from_mysql(self, host, username, password, db, query):
        """
        Extracts data from a MySQL database.

        :param host: The hostname of the MySQL server.
        :param username: The MySQL username.
        :param password: The MySQL password.
        :param db: The name of the database to connect to.
        :param query: The SQL query to execute.
        :return: A list of dictionaries where each dictionary represents a row in the result set.
        """
        if not host or not username or not db or not query:
            raise ValueError("Please provide valid host, username, database, and query.")

        # Connect to MySQL server
        connection = pymysql.connect(
            host=host,
            user=username,
            password=password,
            db=db,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                # Execute the provided query
                cursor.execute(query)
                # Fetch all results
                results = cursor.fetchall()
                return results
        finally:
            # Close the connection
            connection.close()

# Example usage
if __name__ == "__main__":
    # Create an instance of the Extract class
    extractor = Extract()

    # Define your connection parameters and query
    host = 'localhost'
    username = 'root'
    password = 'admin'
    db = 'vinylrecordshop'
    query = 'SELECT * FROM artist;'

    # Extract data
    data = extractor.from_mysql(host, username, password, db, query)
    
    # Print the results
    for row in data:
        print(row)


