from extract import extract  # Updated import statement

# Path to your XML file
xml_file_path = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-Static-Method/newsfeed.xml'

# Use the fromCustom method to execute the extractor
try:
    news_data = extract.fromCustom(extract.xml_extractor, xmlfile=xml_file_path)
    print("Extracted News Items:")
    for news in news_data:
        print(news)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")