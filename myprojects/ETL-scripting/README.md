# Extracting, Transforming, and Loading with ETL Scripting
Create a Python script that automates the process of extracting data from a source, transforming it to meet a data scientist's requirements, and loading it into a destination accessible to the data scientist.

# OBJECTIVES
    • Describe a variety of activities related to ETL.
    • Leverage Python to extract, transform, and load data from various sources.
    • Use Python to create a script that extracts data from one location, transforms the data as necessary, and loads the transformed data into a separate database.
    • Leverage Python and object-oriented programming concepts to create a reusable and compact ETL library.

# ETL SCRIPTING IN PYTHON
    • Access data in a source database or other storage location and load it into a different database or storage location. This process is equivalent to a simple copy and paste of the data from source to target.
    • Access data in the source database or storage, perform some transformation to meet the schema of the target table, and then store the data in the target table. An example of this situation is extracting data from an OLTP database, performing some transformation on the data to meet the schema of the target database, then loading the transformed data into the target database. More specifically, a database of prices stored as dollar values could be pulled, each price could be converted to a different monetary type, and then the updated prices could be loaded into a new database.
    • Extract data that is not stored in a database and move that data to a database. Examples include information stored in text files, spreadsheets, and similar unorganized files. The data is transformed into a format that can be stored in a temporary database and loaded to the target database.

# DESIGN AND IMPLEMENT CUSTOM ETL SCRIPTS
1. Extract must be able to access data from a variety of data sources,including:
    • CSV files
    • SQL tablesMongo
    • DB collections
    • JSON files
      
2. Transform must support several transformations on the data, including:
    • Basic data transformation, such as:
		- Data resizing and reshaping rows (e.g., selecting a limited
		number of columns from the original data)
		- Converting and parsing data (e.g., converting a string into an
		integer or parsing the number part of a string)
    • Column transformation
    • Header manipulation (e.g., changing the column headers)
    • Sorting data
    • Grouping data
    • Concatenating data
    • Detecting and removing duplicates
    • Filling in missing values and replacing erroneous values
      
3. Load must support saving data to a variety of data formats, including:
    • CSV files
    • SQL tables
    • NoSQL tables
    • JSON files

# THE EXTRACT CLASS
Because an ETL process has three main components, it is logical to create a separate class for each activity. We will start with the extract class and define methods that will allow it to extract data from a variety of sources.
	extract.py: The extract class shell
	class extract:
		def fromCSV(self):
			pass
		def fromJSON(self):
			pass
		def fromMYSQL(self):
			pass
		def fromMONGODB(self):
			pass

# Adding the extract.fromCSV Method
We can use inheritance to create the extract class, which will contain all
the methods needed to extract data from different sources. We will start
with the fromCSV method, which we can use to extract data from any CSV
file.

    • It displays a user-friendly message if the file path is not valid.
    • It uses the built-in csv.DictReader method to read the contents of the CSV file.
    • It stores the results in a list named dataset.

# Creating the extract.fromJSON Method
We can also implement a fromJSON method to extract data from JSON files.
 we create a new script with the extract class that adds the new fromJSON method following the same pattern we used for fromCSV. We then test the method using a person.json file.

# Creating the extract.fromMySQL Method
We can now create a new method to extract data from a MySQL database.
The code examples in this lesson assume that MySQL is using the
following settings:
    • host: localhost
    • username: root
    • password: admin

We cannot follow the same pattern we used for CSV and JSON files because extracting data from a MySQL database is more complicated than simply reading a local file. In this case, we will add a new fromMYSQL method to the extract class to perform the following steps:
    • Define the arguments for the method, including information about how to connect to the MySQL server, what database to use, and what query will pull the correct data from the database.
    • Use PyMySQL to retrieve the data using the defined connection parameters.
    • Save the retrieved data to a list.
    • Commit the changes in the database.
    • Close the connection to the database and the database itself.

# Installing the PyMySQL Package
	python3 -m pip install PyMySQL

# Setting Up the DeepaRecordShop Database
	SQL (run in MySQL): deeparecordshop.sql
	Python (run with MySQL running in the background):
		deeparecordshop.py

# Creating the extract.fromMongoDB Method
Finally, we will add the fromMongoDB method to the extract class. To test this script, you must have a MongoDB server running on localhost, with a database named deeparecordshop.db and a collection named musical_instruments. 
    • host: localhost
    • port: 27017
    • username: admin
    • password: admin
You will need to revise the code if your settings are different. Alternatively, you may use the following command in MongoDB to create an administrator account that you can use to connect to MongoDB so that you can use the credentials in the code provided in this lesson:
	use admin;
	db.createUser({user: "admin",pwd: "admin",roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]});

# Verify the extract.py Module
To this point, we have run Python code exclusively as scripts within the IDE. However, we can also store reusable code as Python modules—files stored outside of the current code but that we can call as needed when we run the code. At this point, your extract.py file should include code for all four methods.

# Using Our Script as an External Module
	from extract import extract

# THE TRANSFORM CLASS
	Once the extract class works as expected and we have the extract.py module ready to use, we can start building the transform class.

# Defining the transform Class
We start by creating a transform class template that outlines the steps we plan to use when transforming the extracted data. We create a class template with the following steps:
    • Retrieve some records from the top of the extracted dataset
    • Retrieve some records from the end of the extracted dataset
    • Rename one or more columns
    • Remove one or more unnecessary columns
    • Transform the data itself

# transform.py—the shell for the transform class
class transform:
	def head(self, dataset, step): #return the top N records from the dataset
		pass
	def tail(self): #return the last N records from the dataset
		pass
	def rename_attribute(self): #rename a column in the dataset
		pass
	def remove_attribute(self): #remove a column from the dataset
		pass
	def rename_attributes(self): #rename a list of columns in the dataset
		pass
	def remove_attributes(self): #remove a list of columns in the dataset
		pass
	def transform(self):
		pass



# Creating the head and tail Methods
We start by retrieving only a few records from the top of the extracted dataset and from the end of the extracted dataset. Data engineers often workwith extremely large datasets, and it could be time consuming to use theentire dataset if we just want to verify that the dataset exists or verify what is in it.
We can use steps like this for any of the following:
    • To confirm that there is data in the dataset
    • To see what columns or attributes exist in the dataset
    • To determine what the columns or attributes are named
    • To examine what kind of data is in each column or attribute

# Renaming a Column
One common transformation step is to rename columns or attributes for extracted data. For example, the original name may conflict with the name of an existing column in the target dataset, or we may simply want to use a more descriptive name. In the example, we rename a single column in the target dataset and assign it a different name in the temporary data store created during the transform process.

# Removing a Column from the Data Source
Another common transformation step is to remove one or more attributes from the original data source. Note that this process does not change the original dataset, which we typically want to preserve in case we need it for other uses in the future. Instead, it removes the attribute from the temporary dataset created in the transform process.
In the example, we create a remove_attribute method in the transform class and then use it to remove the Open column.

# Renaming Multiple Columns
While it is useful to rename a single column in the temporary dataset, it is even more useful to be able to rename multiple columns. We can modify the code from the previous example to allow an indefinite number of columns to be renamed. In the example, we create the rename_attributes method that will allow us to rename any number of columns during the transform process.

To get this effect, we create a list to hold the names of the existing columns and a second list to hold the new column names. We verify that the number of columns named is the same for both lists, and then we use a for loop to replace each attribute name in the same order in which they are provided when the method is implemented.

# Removing Multiple Columns
We often want to exclude multiple columns from the original dataset in the transformation process. The existing remove_attribute method works for a single column, but we can also create a method that can remove an indefinite number of columns. 

In the example, we add a remove_attributes method so that the user can name any number of columns to be removed from the extracted dataset. The new method uses a for loop to update the dataset.

# Transforming the Data
The final step in the transform process is to make changes to the data so that the data meets the needs of the target database. This can include transformations like:
    • Rounding numeric values
    • Changing the case of string values
    • Concatenating string values
    • Deconstructing strings or datetime values
    1. Removing out-of-range values, such as nulls or values that are too high or too low for the target specifications
    • Converting strings to numbers or vice versa

The exact transformations depend both on what the original data looks like and the needs of the data scientists who will use the extracted data. The transformation itself will include not only a new method in the transform class, but also one or more functions that the method can call to transform the data.

# THE LOAD CLASS
The final step of an ETL process is to load the transformed data into a relatively permanent storage location so that data scientists and other users can access the data and use it as they need to. As with the extract class we've already defined, we want our ETL script to be able to put the transformed data into a variety of data formats, including CSV, JSON, MySQL, and MongoDB. In the process, we will save the transformed data to an external file.
load.py —the template for the load class
class load:
	def toCSV(self):
		pass
	def toJSON(self):
		pass
	def toMYSQL(self):
		pass
	def toMONGODB(self):
		pass

# Creating the load.toCSV Method
we add the first method to the load class, toCSV, which will load our dataset to a CSV file. You can update your load.py file toinclude the toCSV method.

we can use the extract class to import data from the existing stocks.csv file to a copy of that file, also in CSV format. Note that we do not actually transform the data in any way in
this example, and the result should be an exact copy of the file we started with.

# Creating the load.toJSON Method
Next, let's add a method that will put the extracted data in a JSON file. The new toJSON method in the load class shown the extracted dataset to a new JSON file.

We should update your load.py file to include the new toJSON method. we use the toJSON method. Again, no transformation steps are included here. We simply extract the data from a CSV file and add the same data to a JSON file.

# Creating the load.toMYSQL Method
Update your load.py file to include the toMYSQL method.

Because the load process will add data to an existing table, open a MySQL instance and run the code in to set up a target database and table. Our next example will load data into this new table.

# Creating the Load.toMONGODB Method
Finally, let's look at loading data into a MongoDB database. Update your load.py file to include the toMONGODB class. This listing now contains the code to do all the loads that were originally presented in.

we extract the same stocks.csv file we have used in earlier steps, and we load the data into a new MongoDB collection. Because MongoDB allows us to create a database or a collection by simply naming them, we do not have to set up the database ahead of time.
