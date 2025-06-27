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
# add_scraped_data.py
from database import create_connection
from datetime import date

def insert_scraped_product(product_name, category, brand, retailer_name, retailer_website, price, currency='USD'):
    conn = create_connection()
    cursor = conn.cursor()

    # 1. Insert or get product_id
    cursor.execute("SELECT product_id FROM products WHERE name = ?", (product_name,))
    product = cursor.fetchone()
    if product:
        product_id = product[0]
    else:
        cursor.execute("INSERT INTO products (name, category, brand) VALUES (?, ?, ?)",
                       (product_name, category, brand))
        product_id = cursor.lastrowid

    # 2. Insert or get retailer_id
    cursor.execute("SELECT retailer_id FROM retailers WHERE name = ?", (retailer_name,))
    retailer = cursor.fetchone()
    if retailer:
        retailer_id = retailer[0]
    else:
        cursor.execute("INSERT INTO retailers (name, website) VALUES (?, ?)",
                       (retailer_name, retailer_website))
        retailer_id = cursor.lastrowid

    # 3. Insert price
    today = str(date.today())
    cursor.execute("""
        INSERT INTO prices (product_id, retailer_id, price, currency, date_collected)
        VALUES (?, ?, ?, ?, ?)
    """, (product_id, retailer_id, price, currency, today))

    conn.commit()
    conn.close()
    print(f" Inserted scraped data into database for {product_name} from {retailer_name}")