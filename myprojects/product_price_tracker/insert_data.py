# insert_data.py
# -----------------------------------------------------------------------------------------------------
# Project Name : Product Price Intelligence System
# Author       : Deepa Ponnusamy
# Email        : deepa.ponnusamy@calbrightcollege.org
# GitHub       : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/product_price_tracker
# Date         : May 5, 2025 to June 30, 2025
# Description  : Inserts sample data into a clean SQLite database, avoiding duplicates.
# ----------------------------------------------------------------------------------------------------------
from database import create_connection
def insert_sample_data():
    conn = create_connection()
    cursor = conn.cursor()

    # Clear existing records
    cursor.execute("DELETE FROM prices")
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM retailers")
    conn.commit()

    # Insert products
    products = [
        ('Wireless Mouse', 'Electronics', 'Logitech'),
        ('Noise Cancelling Headphones', 'Audio', 'Sony'),
        ('Portable Charger', 'Accessories', 'Anker'),
        ('Bluetooth Speaker', 'Audio', 'JBL'),
        ('Webcam HD', 'Electronics', 'Logitech'),
        ('Smart Fitness Tracker', 'Wearables', 'Fitbit')
    ]
    cursor.executemany("INSERT INTO products (name, category, brand) VALUES (?, ?, ?)", products)
    conn.commit()

    # Get product_id mapping by name
    cursor.execute("SELECT product_id, name FROM products")
    product_map = {name: pid for pid, name in cursor.fetchall()}

    # Insert retailers
    retailers = [
        ('Amazon', 'https://www.amazon.com'),
        ('Best Buy', 'https://www.bestbuy.com'),
        ('Walmart', 'https://www.walmart.com'),
        ('Target', 'https://www.target.com'),
        ('Newegg', 'https://www.newegg.com'),
        ('eBay', 'https://www.ebay.com'),
        ('Demo Store', 'http://demo.local')
    ]
    cursor.executemany("INSERT INTO retailers (name, website) VALUES (?, ?)", retailers)
    conn.commit()

    # Get retailer_id mapping by name
    cursor.execute("SELECT retailer_id, name FROM retailers")
    retailer_map = {name: rid for rid, name in cursor.fetchall()}

    from datetime import date
    today = str(date.today())

    # Now use mapped IDs to insert prices
    prices = [
        (product_map['Wireless Mouse'], retailer_map['Amazon'], 25.99, 'USD', today),
        (product_map['Wireless Mouse'], retailer_map['Best Buy'], 27.49, 'USD', today),
        (product_map['Wireless Mouse'], retailer_map['Target'], 26.89, 'USD', today),

        (product_map['Noise Cancelling Headphones'], retailer_map['Amazon'], 199.99, 'USD', today),
        (product_map['Noise Cancelling Headphones'], retailer_map['Newegg'], 189.49, 'USD', today),

        (product_map['Portable Charger'], retailer_map['Walmart'], 39.99, 'USD', today),
        (product_map['Portable Charger'], retailer_map['eBay'], 35.99, 'USD', today),

        (product_map['Bluetooth Speaker'], retailer_map['Amazon'], 79.99, 'USD', today),
        (product_map['Bluetooth Speaker'], retailer_map['Best Buy'], 76.49, 'USD', today),
        (product_map['Bluetooth Speaker'], retailer_map['Newegg'], 74.99, 'USD', today),

        (product_map['Webcam HD'], retailer_map['Amazon'], 49.99, 'USD', today),
        (product_map['Webcam HD'], retailer_map['Best Buy'], 47.99, 'USD', today),
        (product_map['Webcam HD'], retailer_map['Target'], 46.50, 'USD', today),

        (product_map['Smart Fitness Tracker'], retailer_map['Amazon'], 99.99, 'USD', today),
        (product_map['Smart Fitness Tracker'], retailer_map['Target'], 95.50, 'USD', today),
        (product_map['Smart Fitness Tracker'], retailer_map['eBay'], 92.99, 'USD', today),
    ]

    cursor.executemany("""
        INSERT INTO prices (product_id, retailer_id, price, currency, date_collected)
        VALUES (?, ?, ?, ?, ?)
    """, prices)

    conn.commit()
    conn.close()