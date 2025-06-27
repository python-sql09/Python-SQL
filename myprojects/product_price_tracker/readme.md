# Product Price Intelligence System

This is a SQLite-based system that stores and retrieves product pricing data from multiple online retailers. It supports price comparisons and can be extended for integration with real-world web scraping tools or e-commerce APIs.

### Features
- Structured SQLite schema
- Insert and retrieve product data
- Price comparison report (best price per product)
- Modular code with clean separation

### Tools Used
- Python 3
- SQLite
- PyCharm IDE

### How to Run
1. Clone or download this project.
2. Open it in PyCharm.
3. Make sure you have required Python packages installed:
	 * pip install streamlit pandas beautifulsoup4
4. Run main.py once to initialize DB and insert sample data:
     * python main.py
5. Run Streamlit dashboard:
     * streamlit run price_dashboard.py
6. Run scraper test if you want to test scraping local HTML:
     * python demo_scrape_test.py
   
### Author
Deepa Ponnusamy  
[GitHub Portfolio](https://github.com/python-sql09/tree/main/myprojects/product_price_tracker)