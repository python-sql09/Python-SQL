import xml.etree.ElementTree as ET

class CustomStatic:
    @staticmethod
    def fromCustom(custom_extractor, **kwds):
        dataset = custom_extractor(**kwds)
        if type(dataset) != list:
            raise ValueError("Output data from extract step should be a list of items.")
        return dataset

def xml_extractor(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    newsitems = []
    for item in root.findall('./channel/item'):
        news = {}
        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        newsitems.append(news)
    return newsitems

# Path to your XML file
xml_file_path = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/custom-class/newsfeed.xml'

# Use the fromCustom method to execute the extractor
try:
    dataset = CustomStatic.fromCustom(xml_extractor, xmlfile=xml_file_path)
    print("Extracted News Items:")
    for news in dataset:
        print(news)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")