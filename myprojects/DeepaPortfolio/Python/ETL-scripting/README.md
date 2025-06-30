# 1 extract.py: The extract class shell
class extract:
    def fromCSV(self):
        pass
    def fromJSON(self):
        pass
    def fromMYSQL(self):
        pass
    def fromMONGODB(self):
        pass

These package files will be saved using the .py filename extension, independently of any code running in the current window, but in the same folder as the current code. Create a new file named extract.py in the same folder as your code files for this lesson and add the template code from Listing #1 to that file.

Adding the extract.fromCSV Method
----------------------------------
We can use inheritance to create the extract class, which will contain all the methods needed to extract data from different sources. We will start with the fromCSV method,
which we can use to extract data from any CSV file.

We will use the extract.fromCSV method as a model for extracting data from other types of sources.

•• It displays a user-­friendly message if the file path is not valid.
•• It uses the built-­in csv.DictReader method to read the contents of the CSV file.
•• It stores the results in a list named dataset. The script in Listing #2 also displays the contents of the extracted dataset to verify that it works as expected. We use a CSV file called got_chars.csv that you can download
from https://the-­software-­guild.s3.amazonaws.com/datascience/track1-­1909/got_chars.csv; however, you can use any available CSV file to test the script.

# 2 Creating the fromCSV method
class extract:
    def fromCSV(self, file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter = delimiter, quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset

    def fromJSON(self):
        pass

    def fromMYSQL(self):
        pass

    def fromMONGODB(self):
        pass

e = extract()
dataset = e.fromCSV(file_path="/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/got_chars.csv")
for row in dataset:
    print(row)

Creating the extract.fromJSON Method
------------------------------------
We can also implement a fromJSON method to extract data from JSON files. In Listing #3. we create a new script with the extract class that adds the new fromJSON method follow ing the same pattern we used for fromCSV. We then test the method using a person.json file

# 3 Creating the fromJSON method
class extract:
    def fromCSV(self, file_path, delimiter = ",", quotechar = "|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter = delimiter, quotechar = quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset
    
    def fromJSON(self, file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

    def fromMYSQL(self):
        pass
    
    def fromMONGODB(self):
        pass

e = extract()
dataset = e.fromJSON(file_path = "/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/person.json")
print(dataset)
print(len(dataset))

Creating the extract.fromMySQL Method
-------------------------------------
We can now create a new method to extract data from a MySQL database. The code examples in this lesson assume that MySQL is using the following settings:
•• host: localhost
•• username: root
•• password: admin
You may need to adjust the code if your MySQL server uses different login settings. We cannot follow the same pattern we used for CSV and JSON files because extracting data from a MySQL database is more complicated than simply reading a local file. In this case, we will add a new fromMYSQL method to the extract class to perform the following steps:
•• Define the arguments for the method, including information about how to connect to the MySQL server, what database to use, and what query will pull the correct data from the database.
•• Use PyMySQL to retrieve the data using the defined connection parameters.
•• Save the retrieved data to a list.
•• Commit the changes in the database.
•• Close the connection to the database and the database itself.
To test this script, you must have the PyMySQL package installed as well as have a MySQL server running on localhost, with a database named vinylrecordshop and a table named artist