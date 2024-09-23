# 10 Custom class to extract from an XML file
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
if __name__ == "__main__":
    xmlfile = '/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/sample_rss_feed.xml'  # Update this path
    news = xml_extractor(xmlfile)
    if news:
        for idx, item in enumerate(news, start=1):
            print(f"News Item {idx}:")
            for key, value in item.items():
                print(f"  {key}: {value}")
    else:
        print("No news items found or an error occurred.")


                