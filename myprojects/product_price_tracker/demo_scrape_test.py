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
# demo_scraper_test.py
# ------------------------------------------------------------------
# Test script for scraper.py + database insertion
# ------------------------------------------------------------------

from scraper import fetch_price_from_demo_file

if __name__ == "__main__":
    filepath = "demo_product.html"  # Make sure this file is present in the project directory

    result = fetch_price_from_demo_file(filepath)

    if result:
        product, price = result
        print(f"🎯 Final Result -> Product: {product} | Price: ${price}")
    else:
        print("❗ No product information extracted.")