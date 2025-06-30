# insert_data.py
# -----------------------------------------------------------------------------------------------------
# Project Name : Product Price Intelligence System
# Author       : Deepa Ponnusamy
# Email        : deepa.ponnusamy@calbrightcollege.org
# GitHub       : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/product_price_tracker
# Date         : June 22, 2025
# Description  : A price comparison tool that builds a structured SQLite database
#                to collect, store, and retrieve pricing data from online retailers.
#                Supports efficient product lookups, integrates with future
#                application infrastructure, and demonstrates database schema design,
#                data insertion, and querying logic.
# ----------------------------------------------------------------------------------------------------------
from database import create_connection
from datetime import date

def insert_sample_data():
    conn = create_connection()
    cursor = conn.cursor()

    # Insert products
    products = [
        ('Wireless Mouse', 'Electronics', 'Logitech'),
        ('Noise Cancelling Headphones', 'Audio', 'Sony'),
        ('Portable Charger', 'Accessories', 'Anker'),
        ('Bluetooth Speaker', 'Audio', 'JBL'),
        ('Webcam HD', 'Electronics', 'Logitech'),
        ('Smart Fitness Tracker', 'Wearables', 'Fitbit')  # New product added
    ]
    cursor.executemany("INSERT INTO products (name, category, brand) VALUES (?, ?, ?)", products)

    # Insert retailers
    retailers = [
        ('Amazon', 'https://www.amazon.com'),
        ('Best Buy', 'https://www.bestbuy.com'),
        ('Walmart', 'https://www.walmart.com'),
        ('Target', 'https://www.target.com'),
        ('Newegg', 'https://www.newegg.com'),
        ('eBay', 'https://www.ebay.com')  # Added more retailers for diversity
    ]
    cursor.executemany("INSERT INTO retailers (name, website) VALUES (?, ?)", retailers)

    # Insert prices
    prices = [
        # Wireless Mouse
        (1, 1, 25.99, 'USD', str(date.today())),
        (1, 2, 27.49, 'USD', str(date.today())),
        (1, 4, 26.89, 'USD', str(date.today())),

        # Noise Cancelling Headphones
        (2, 1, 199.99, 'USD', str(date.today())),
        (2, 5, 189.49, 'USD', str(date.today())),

        # Portable Charger
        (3, 3, 39.99, 'USD', str(date.today())),
        (3, 6, 35.99, 'USD', str(date.today())),

        # Bluetooth Speaker
        (4, 1, 79.99, 'USD', str(date.today())),
        (4, 2, 76.49, 'USD', str(date.today())),
        (4, 5, 74.99, 'USD', str(date.today())),

        # Webcam HD
        (5, 1, 49.99, 'USD', str(date.today())),
        (5, 2, 47.99, 'USD', str(date.today())),
        (5, 4, 46.50, 'USD', str(date.today())),

        # Smart Fitness Tracker - NEW
        (6, 1, 99.99, 'USD', str(date.today())),
        (6, 4, 95.50, 'USD', str(date.today())),
        (6, 6, 92.99, 'USD', str(date.today())),
    ]
    cursor.executemany(
        "INSERT INTO prices (product_id, retailer_id, price, currency, date_collected) VALUES (?, ?, ?, ?, ?)",
        prices
    )

    conn.commit()
    conn.close()