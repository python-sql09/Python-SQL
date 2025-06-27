# ---------------------------------------------------------------------------------------------------------
# Project Name : Product Price Intelligence System
# Author       : Deepa Ponnusamy
# Email        : deepa.ponnusamy@calbrightcollege.org
# GitHub       : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/product_price_tracker
# Date         : May 5, 2025 to June 30, 2025
# Description  : Simulates fetching product name and price from a local HTML file
#                using BeautifulSoup for demonstration purposes.
# ---------------------------------------------------------------------------------------------------------
# scraper.py
from bs4 import BeautifulSoup

def fetch_price_from_demo_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')

        product = soup.find('h1', {'class': 'product-name'}).text.strip()
        price_text = soup.find('span', {'class': 'price'}).text.strip()
        price = float(price_text.replace('$', ''))

        print(f"✅ Scraped from local file: {product} | Price: ${price:.2f}")
        return product, price

    except Exception as e:
        print(f"❌ Error scraping product: {e}")
        return None