# 10 Defining head and tail methods
# head - top N records, tail - Botton(last) N records
from extract import extract #import our custom built extract module
class transform:
    #return the top N records from the dataset
    def head(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[0:step]
    #return the last N records from the dataset
    def tail(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[len(dataset) - step:len(dataset)]
    e = extract()
    # connect to mongodb; change values if necessary
    dataset = e.fromMONGODB(host = "localhost", port = 27017, username = "admin",
    password = "admin", db = "amazon_reviews",
    collection = "musical_instruments")
    t = transform()
    dataset_1 = t.head(dataset = dataset, step = 5) # retrieve the top 5 records
    # in the dataset
    print("Top 5 records in the dataset:")
    for row in dataset_1:
        print(row['_id'])
    dataset_2 = t.tail(dataset = dataset, step = 5) #retrieve the bottom 5 records
    #in the dataset
    print("\nBottom 5 records in the dataset:")
    for row in dataset_2:
        print(row['_id'])
    