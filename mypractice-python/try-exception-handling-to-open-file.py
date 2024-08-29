# 22.13 Adding exception handling to opening a file
def read_csv(filepath,delimiter=","):
    import csv
    dataset = list()
    try:
        with open(filepath) as f: # Use open function to read the C.csv file
            # and create a file object f
            # Use the reader function under the csv module to read the
            # file using comma a delimiter
            csv_file = csv.DictReader(f, delimiter=delimiter)
            # csv_file is an iterable object that we can iterate on using a for loop
            for row in csv_file:
                dataset.append(row)
        return dataset
    except IOError as e:
        print("Unable to access file.")
a = read_csv("file.txt","r") #do not change this line