# main.py
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
# ---------------------------------------------------------------------------------------------------------

from database import initialize_database
from insert_data import insert_sample_data
import sqlite3
import csv

def get_best_prices():
    conn = sqlite3.connect("pricing_db.db")
    cursor = conn.cursor()
    query = """
    SELECT p.name, MIN(pr.price) as best_price
    FROM prices pr
    JOIN products p ON p.product_id = pr.product_id
    GROUP BY p.name
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def print_best_prices(results):
    print("\nBest Prices:\n")
    for row in results:
        print(f"Product: {row[0]} | Best Price: ${row[1]:.2f}")

def search_product(product_name):
    conn = sqlite3.connect("pricing_db.db")
    cursor = conn.cursor()
    query = """
    SELECT p.name, r.name, pr.price, pr.currency, pr.date_collected
    FROM prices pr
    JOIN products p ON p.product_id = pr.product_id
    JOIN retailers r ON r.retailer_id = pr.retailer_id
    WHERE LOWER(p.name) LIKE LOWER(?)
    """
    cursor.execute(query, (f"%{product_name}%",))
    results = cursor.fetchall()
    conn.close()

    if results:
        print(f"\nSearch Results for '{product_name}':\n")
        for row in results:
            print(f"Product: {row[0]} | Retailer: {row[1]} | Price: ${row[2]:.2f} {row[3]} | Date: {row[4]}")
    else:
        print(f"\nNo results found for '{product_name}'.")

def export_best_prices_to_csv(results, filename="best_prices.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "Best Price"])
        writer.writerows(results)
    print(f"\n\U0001F4C1 Exported best prices to '{filename}'")

def print_sample_data():
    conn = sqlite3.connect("pricing_db.db")
    cursor = conn.cursor()
    print("\nSample products:")
    for row in cursor.execute("SELECT product_id, name FROM products LIMIT 5"):
        print(row)
    print("\nSample retailers:")
    for row in cursor.execute("SELECT retailer_id, name FROM retailers LIMIT 5"):
        print(row)
    print("\nSample prices:")
    for row in cursor.execute("SELECT product_id, retailer_id, price FROM prices LIMIT 5"):
        print(row)
    conn.close()

if __name__ == "__main__":
    initialize_database()
    insert_sample_data()
    print_sample_data()  # Verify inserted data
    best_prices = get_best_prices()
    print_best_prices(best_prices)
    search_product("Mouse")
    export_best_prices_to_csv(best_prices)