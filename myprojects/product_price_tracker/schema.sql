-- ---------------------------------------------------------------------------------------------------------
-- Project Name : Product Price Intelligence System
-- Author       : Deepa Ponnusamy
-- Email        : deepa.ponnusamy@calbrightcollege.org
-- GitHub       : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/product_price_tracker
-- Date         : May 5, 2025 to June 30, 2025
-- Description  : A price comparison tool that builds a structured SQLite database
--               to collect, store, and retrieve pricing data from online retailers.
--               Supports efficient product lookups, integrates with future
--               application infrastructure, and demonstrates database schema design,
--                data insertion, and querying logic.
-- ---------------------------------------------------------------------------------------------------------

-- Table to store product information
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT,
    brand TEXT
);

-- Table to store retailer information
CREATE TABLE IF NOT EXISTS retailers (
    retailer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    website TEXT
);

-- Table to store prices
CREATE TABLE IF NOT EXISTS prices (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    retailer_id INTEGER,
    price REAL,
    currency TEXT,
    date_collected TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (retailer_id) REFERENCES retailers(retailer_id)
);

-- ------------------------------------------------------------------
-- Indexes for faster search and joins
-- ------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_prices_product_id ON prices (product_id);
CREATE INDEX IF NOT EXISTS idx_prices_retailer_id ON prices (retailer_id);
CREATE INDEX IF NOT EXISTS idx_products_name ON products (name);