# 3 Converting classes to static in the transform class
from extract import extract
class transform:
    #return the top N records from the dataset
    @staticmethod
    def head(dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[0:step]

    #return the last N records from the dataset
    @staticmethod
    def tail(dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if step < 1:
            raise Exception("The step value must be positive.")
        return dataset[len(dataset) - step:len(dataset)]

    #rename a column in the dataset
    @staticmethod
    def rename_attribute(dataset, attribute, new_attribute):
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
                raise Exception("Operation is not possible because the column "
                        + str(column_name)
                        + " does not exist in one of the rows in the dataset.")
        return new_dataset

    #remove a column from the dataset
    @staticmethod
    def remove_attribute(dataset, attribute):
        new_dataset = list()
        for row in dataset:
            new_row = row
            if attribute in new_row.keys():
                del new_row[attribute]
                new_dataset.append(new_row)
        return new_dataset

    @staticmethod
    def rename_attributes(dataset, attributes, new_attributes):
        if not attributes or not new_attributes:
            raise Exception("The attributes cannot be empty.")
        if len(attributes) != len(new_attributes):
            raise Exception("The number of new column names must match the number of \
                existing column names.")
        new_dataset = list()
        for row in dataset:
            new_row = row
            for i in range(0,len(attributes)):
                attribute = attributes[i]
                new_attribute = new_attributes[i]
                if attribute in new_row.keys():
                    val = row[attribute]
                    del new_row[attribute]
                    new_row[new_attribute] = val
                else:
                    raise Exception("Operation is not possible because the key "
                            + str(key)+
                            " does not exist in one of the rows in the dataset.")
            new_dataset.append(new_row)
        return new_dataset

    #remove a column from the dataset
    @staticmethod
    def remove_attributes(dataset, attributes):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
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
    
    @staticmethod
    def transform(dataset, attribute, new_attribute, transform_function, *args):
        if not dataset:
            raise Exception("Dataset cannot be empty.")
        if not attribute or not new_attribute:
            raise Exception("The input attribute cannot be empty.")
        if not transform_function:
            raise Exception("The transform_function cannot be None.")
        new_dataset = list() #output of this function
        for row in dataset: #iterate through the input data
            t = transform_function(row[attribute], *args) #apply transformation
                    #function on column
            z = row.copy()
            z.update({new_attribute:t}) #create new column in the data
            new_dataset.append(z)
        return new_dataset

    def round_open_price(value,*args):
        return round(float(value))
    dataset = extract.fromCSV(file_path = "python-sql09/Python-SQL/mypractice-python/data/stocks.csv")
    print(dataset[0])
    new_dataset = transform.transform(dataset = dataset, attribute = "Open",
                                      new_attribute = "open_price_rounded",
                                      transform_function = round_open_price)
    print(new_dataset[0])