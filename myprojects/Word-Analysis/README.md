Word Analysis in Python
------------------------
When we start any data analysis process, the first step is to ensure that the data is in a format that our system can use and that the data is available for use. For our project, we will need to download the data. We will use the Digital Music review set from Julian McCauley’s Amazon product data website, which you can find at http://jmcauley .ucsd.edu/data/amazon/. This file, reviews.json

READ THE DATA
-------------
Now that we have looked at the data and identified what we want our code to do, we’re ready to start writing code. Create two new files in the same folder where the .json data file is stored:
•• main.py
•• lib.py

# lib.py
# 1. The start of our lib.py file
import json
def read_json_file(path):
    dataset = list()
    with open(path) as json_file:
        for line in json_file:
            dataset.append(json.loads(line))
    return dataset

In this code, we import Python’s JSON package to manage the JSON input. We then
create the read_json_file function that takes a file path as input. An empty list named dataset is then created before data is read into the list. As data is read, each line of text (each review) in the JSON file is converted to a dictionary (using json.loads) and then the dictionary (the review) is added to the dataset. The function returns a list in which each item in the list is a record from the original JSON file.

# main.py
# 2. The main function to run function to read a JSON file
from lib import *
dataset = read_json_file("reviews.json") #read file
print(dataset[0])

We need to tweak the function a little to make it more user-­friendly. When we ask the user to input a file, any of three things can happen:
1. They enter a complete and correct path, which works the way we expect it to.
2. They forget to enter a path.
3. They enter the wrong path.