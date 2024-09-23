# 10 Custom class to extract from an XML file
def xml_extractor(xmlfile):
    import xml.etree.ElementTree as ET
    try:
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        
        # Optional: Print root and child tags for debugging
        print(f"Root tag: {root.tag}")
        for child in root:
            print(f"Child tag: {child.tag}")
        
        # Define namespaces if needed
        namespaces = {'media': 'http://search.yahoo.com/mrss/'}
        
        newsitems = []
        for item in root.findall('./channel/item', namespaces):
            print("Processing an item")  # Debugging line
            news = {}
            for child in item:
                if child.tag == '{http://search.yahoo.com/mrss/}content':
                    news['media'] = child.attrib.get('url', '')
                else:
                    tag = child.tag.split('}', 1)[1] if '}' in child.tag else child.tag
                    news[tag] = child.text
            newsitems.append(news)
        return newsitems
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except FileNotFoundError:
        print(f"File not found: {xmlfile}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    xmlfile = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/custom-class/sample_rss_feed.xml'  # Update this path
    news = xml_extractor(xmlfile)
    if news:
        for idx, item in enumerate(news, start=1):
            print(f"News Item {idx}:")
            for key, value in item.items():
                print(f"  {key}: {value}")
    else:
        print("No news items found or an error occurred.")
