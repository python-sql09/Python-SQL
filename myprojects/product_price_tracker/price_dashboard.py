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
# price_dashboard.py
# ------------------------------------------------------------------
# Streamlit Dashboard to View and Search Product Prices
# ------------------------------------------------------------------

import streamlit as st
import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect("pricing_db.db")

def get_best_prices():
    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT p.name AS Product, MIN(pr.price) AS Best_Price
        FROM prices pr
        JOIN products p ON p.product_id = pr.product_id
        GROUP BY p.name
    """, conn)
    conn.close()
    return df

def get_all_products():
    conn = get_connection()
    df = pd.read_sql_query("SELECT name FROM products", conn)
    conn.close()
    return df["name"].tolist()

def get_all_retailers():
    conn = get_connection()
    df = pd.read_sql_query("SELECT name FROM retailers", conn)
    conn.close()
    return df["name"].tolist()

def search_product(product_name="", retailer_name=""):
    conn = get_connection()
    query = """
    SELECT p.name AS Product, r.name AS Retailer, pr.price AS Price,
           pr.currency AS Currency, pr.date_collected AS Date
    FROM prices pr
    JOIN products p ON p.product_id = pr.product_id
    JOIN retailers r ON r.retailer_id = pr.retailer_id
    WHERE p.name LIKE ? AND r.name LIKE ?
    """
    df = pd.read_sql_query(query, conn, params=(f"%{product_name}%", f"%{retailer_name}%"))
    conn.close()
    return df

st.set_page_config(page_title="💲 Price Intelligence", layout="wide")
st.title("🛍️ Product Price Intelligence Dashboard")

tab1, tab2, tab3 = st.tabs(["📌 Best Prices", "🔍 Filter & Search", "📊 Price Chart"])

with tab1:
    st.subheader("📉 Best Prices by Product")
    best_prices_df = get_best_prices()
    st.dataframe(best_prices_df, use_container_width=True)

    csv = best_prices_df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download as CSV", csv, "best_prices.csv", "text/csv")

with tab2:
    st.subheader("🔍 Filter Products & Retailers")
    col1, col2 = st.columns(2)

    with col1:
        selected_product = st.selectbox("Select Product", [""] + get_all_products())
    with col2:
        selected_retailer = st.selectbox("Select Retailer", [""] + get_all_retailers())

    if selected_product or selected_retailer:
        filtered_df = search_product(selected_product, selected_retailer)
        if not filtered_df.empty:
            st.dataframe(filtered_df, use_container_width=True)
        else:
            st.warning("⚠️ No results for your selection.")

with tab3:
    st.subheader("📊 Visualize Best Prices")
    chart_df = get_best_prices()
    st.bar_chart(data=chart_df.set_index("Product"), use_container_width=True)