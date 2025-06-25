# main.py
# ---------------------------------------------------------------------------------------------------------
# Project Name : Product Price Intelligence System
# Author       : Deepa Ponnusamy
# Email        : deepa.ponnusamy@calbrightcollege.org
# GitHub       : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/product_price_tracker
# Date         : June 21, 2025
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
    WHERE p.name LIKE ?
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
    print(f"\n📁 Exported best prices to '{filename}'")


if __name__ == "__main__":
    initialize_database()
    insert_sample_data()

    # Step 1: Get and print best prices
    best_prices = get_best_prices()
    print_best_prices(best_prices)

    # Step 2: Search by keyword
    search_product("Mouse")

    # Step 3: Export to CSV
    export_best_prices_to_csv(best_prices)