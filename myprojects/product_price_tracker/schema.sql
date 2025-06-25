-- schema.sql

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