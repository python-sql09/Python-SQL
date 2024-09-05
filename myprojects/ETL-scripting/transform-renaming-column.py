# 12 Renaming a column
from extract import extract #import our custom built extract module
class transform:
    #rename a column in the dataset
    def rename_attribute(self, dataset, attribute, new_attribute):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if not attribute:
            raise Exception("The attribute key must be a valid key.")
        new_dataset = list()
        for row in dataset:
            if attribute in row.keys():
                val = row[attribute]
                new_row = row.copy()
                del new_row[attribute]
                new_row[new_attribute] = val
                new_dataset.append(new_row)
            else:
                raise Exception("Operation is not possible because the \
column " + str(column_name) + " does not exist in one of the rows \
in the dataset")
        return new_dataset
    e = extract()
    dataset = e.fromCSV(file_path="data/got_chars.csv")
    print("Dataset before renaming the column:")
    print(dataset[0])
    t = transform()
    new_dataset = t.rename_attribute(dataset = dataset, attribute = "character",
    new_attribute = "character_name")
    print("\nDataset after renaming the column:")
    print(new_dataset[0])