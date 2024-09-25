# main.py
from custom_XML import xml_extractor  # Updated import statement
from custom_static import custom_class  # Replace with your actual class name

# Path to your XML file
xml_file_path = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/custom-class/newsfeed.xml'

# Use the fromCustom method to execute the extractor
try:
    news_data = custom_class.fromCustom(xml_extractor, xmlfile=xml_file_path)
    print("Extracted News Items:")
    for news in news_data:
        print(news)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")