# 12 Using the fromCustom method
class extract:
    @staticmethod
    def fromCSV(file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter = delimiter,quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset

    @staticmethod
    def fromJSON(file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

    @staticmethod
    def fromMYSQL(host, username, password, db, query):
        if not host or not username or not db or not query:
            raise Exception("Please make sure that you input a valid host, username, \
                            password, database, and query.")
        import pymysql
        db = pymysql.connect(host = host, user = username, password = password,
                                db = db, cursorclass = pymysql.cursors.DictCursor)
        cur = db.cursor()
        cur.execute(query)
        dataset = list()
        for r in cur:
            dataset.append(r)
        db.commit()
        cur.close()
        db.close()
        return dataset

    @staticmethod
    def fromMONGODB(host, port, username, password, db, collection, query = None):
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, username, \
                            password, database, and collection name")
        import pymongo
        client = pymongo.MongoClient(host = host, port = port,username = username,
                                        password = password)
        tmp_database = client[db]
        tmp_collection = tmp_database[collection]
        dataset = list()
        if query:
            for document in tmp_collection.find(query):
                dataset.append(document)
            return dataset
        for document in tmp_collection.find():
            dataset.append(document)
        return dataset

    # new custom extract method
    @staticmethod
    def fromCustom(custom_extractor,**kwds):
        #we do not check for path. Path must be defined in the standalone function.
        #this will execute the custom_extractor and store the data in dataset.
        dataset = custom_extractor(**kwds)
        #if the type of dataset is not a list then we need to throw an error
        if type(dataset)!= list:
            raise ValueError("Output data from extract step should be a list of items.")
        return dataset

    #standalone function to extract data from XML
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
dataset = extract.fromCustom(extract.xml_extractor,xmlfile="/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-custom/newsfeed.xml")
print(dataset[0])