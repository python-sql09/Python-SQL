# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/ETL-scripting
# Date        : March 27, 2025 to May 3, 2025
# Description : Using toMYSQL method to load test db
# ----------------------------------------------------------------------------------------------------
import sys
sys.path.append('/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting')
from extract import extract  # import your custom-built extract module    

class Load:
    def toMYSQL(self, host, username, password, db, table, dataset):
        if not dataset:
            raise Exception("Input dataset must have at least one item.")
        if not db:
            raise Exception("You must input a valid database name.")
        if not table:
            raise Exception("You must input a valid table name")

        import pymysql
        connection = pymysql.connect(host=host, user=username, password=password, db=db,
                                     cursorclass=pymysql.cursors.DictCursor)

        # Column mapping from CSV to MySQL
        column_mapping = {
            'Adj Close': 'close',  # 'Adj Close' in CSV maps to 'close' in MySQL
            'Date': 'date',        # 'Date' in CSV maps to 'date' in MySQL
            'Open': 'open',
            'High': 'high',
            'Low': 'low',
            'Close': 'close',
            'Volume': 'volume'
        }

        # Valid columns for MySQL table 'cstocks'
        valid_columns = ['date', 'open', 'high', 'low', 'close', 'volume']

        try:
            cur = connection.cursor()

            # Print the dataset to debug the contents
            print("Dataset:", dataset)

            for row in dataset:
                # Apply column mapping
                mapped_row = {column_mapping.get(col, col): value for col, value in row.items()}

                # Filter to only include valid columns
                filtered_row = {col: value for col, value in mapped_row.items() if col in valid_columns}

                # Debugging output to check for 'date' column
                if 'date' not in filtered_row:
                    print(f"Row without 'date': {filtered_row}")
                    raise Exception(f"Missing 'date' column in row: {filtered_row}")

                # Prepare the SQL query
                placeholder = ", ".join(["%s"] * len(filtered_row))
                columns = ", ".join([f"`{col}`" for col in filtered_row.keys()])  # Add backticks around column names
                stmt = f"INSERT INTO {table} ({columns}) VALUES ({placeholder});"
                cur.execute(stmt, list(filtered_row.values()))

            connection.commit()  # Commit the transaction
        finally:
            cur.close()
            connection.close()

# Extract dataset from CSV and load to MySQL
e = extract()
dataset = e.fromCSV(file_path='stocks1.csv', delimiter=',')
l = Load()
l.toMYSQL(host="localhost", username="root", password="Deepa@369", db="test", table="cstocks", dataset=dataset)