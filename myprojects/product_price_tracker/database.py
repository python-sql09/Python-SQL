# database.py
# ---------------------------------------------------------------------------------------------------------
# Project Name : Product Price Intelligence System
# Author       : Deepa Ponnusamy
# Email        : deepa.ponnusamy@calbrightcollege.org
# GitHub       : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/product_price_tracker
# Date         : May 5, 2025 to June 30, 2025
# Description  : A price comparison tool that builds a structured SQLite database
#                to collect, store, and retrieve pricing data from online retailers.
#                Supports efficient product lookups, integrates with future
#                application infrastructure, and demonstrates database schema design,
#                data insertion, and querying logic.
# ----------------------------------------------------------------------------------------------------------
import sqlite3

def create_connection(db_file="pricing_db.db"):
    return sqlite3.connect(db_file)

def initialize_database():
    conn = create_connection()
    with open("schema.sql", "r") as schema_file:
        conn.executescript(schema_file.read())
    conn.commit()
    conn.close()
