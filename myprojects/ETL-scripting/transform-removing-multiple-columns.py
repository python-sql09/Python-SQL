# 16 Removing multiple columns
from extract import extract #import our custom built extract module
class transform:
    #remove multiple column from the dataset
    def remove_attributes(self, dataset, attributes):
        if not dataset:
            raise Exception("Dataset cannot be empty")
        if not attributes:
            raise Exception("The list of attributes cannot be empty.")
        new_dataset= list()
        for row in dataset:
            new_row = row
            for attribute in attributes:
                if attribute in new_row.keys():
                    del new_row[attribute]
            new_dataset.append(new_row)
        return new_dataset
    e = extract()
    dataset = e.fromCSV(file_path = "data/stocks.csv")
    print("Original dataset:")
    print(dataset[0])
    t = transform()
    new_dataset = t.remove_attributes(dataset = dataset, attributes = ["Open","Close"])
    print("\nTransformed dataset:")
    print(new_dataset[0])