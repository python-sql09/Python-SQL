# 13 Using fromCustom via an imported extract class
from extract import extract
def xml_extractor(xmlfile):
    import xml.etree.ElementTree as ET
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()
    # create empty list for news items
    newsitems = []
    # iterate news items
    for item in root.findall('./channel/item'):
        # empty news dictionary
        news = {}
        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        # append news dictionary to news items list
        newsitems.append(news)
    # return news items list
    return newsitems
dataset = extract.fromCustom(xml_extractor,xmlfile="/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-custom/newsfeed.xml")
print(dataset[0])