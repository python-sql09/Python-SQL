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
dataset = read_json_file("/home/linuxdeepa/python-sql09/Python-SQL/myprojects/Word-Analysis/reviews.json") #read file
print(dataset[0])

We need to tweak the function a little to make it more user-­friendly. When we ask the user to input a file, any of three things can happen:
1. They enter a complete and correct path, which works the way we expect it to.
2. They forget to enter a path.
3. They enter the wrong path.

we’ll address the missing path first.
# 3. Dealing with a missing path
def read_json_file(path):
    if not path:
        raise Exception("You must provide a valid file path.")
    dataset = list()
    with open(path) as json_file:
        for line in json_file:
            dataset.append(json.loads(line))
    return dataset

In this update to the lib.py file, we’ve added a check to determine if the file (path) exists. If it does not, an exception is thrown.

remove the filename from main.py as shown in #4 and run the program again.

# 4. Updating main to receive a blank (bad) file
dataset = read_json_file("") #read file
print(dataset[0])

Because there isn’t a file being passed that can be found, the program should print out the exception message defined in the code as such:
Exception: You must provide a valid file path.

let’s address the problem if the input file is not a JSON file, using a try-­except block. #5 updates the read_json_file function to include exception handling for a couple of errors.

# 5. Adding exception handling to our function
def read_json_file(path):
    if not path:
        raise Exception("You must provide a valid file path.")
    try:
        dataset = list()
        with open(path) as json_file:
            for line in json_file:
                dataset.append(json.loads(line))
    except (IOError, OSError):
        raise Exception("You must provide a valid JSON file.")
    return dataset

our new read_json_file function, we embed the existing code in a try block. We then create a user-­friendly message that will display to the user if the path value is not correct and does not point to a JSON file. We can update our main file to run the code with a slightly different filename such as the one shown in #6.

# 6. Using a slightly different filename
dataset = read_json_file("reviews.json") #read file
print(dataset[0])

TOKENIZE THE DATASET
--------------------
In order to tokenize the dataset (meaning tokenizing each review in the dataset), we will adopt the following layered logic:
•• First, implement a function that tokenizes an input string.
•• Input for this function is a simple string.
•• This function will form the base of the next two functions.
•• Second, implement a function that tokenizes an input review from our dataset.
•• Input for this function is a single review (dictionary) from our dataset.
•• This function will simply identify the review text in the review and call the first function to tokenize the text.
•• This function will also add the tokenized words to the review in a new key that we will provide.
•• Finally, implement a function that tokenizes the entire dataset by iterating through each review in the dataset and tokenizing it.
•• Input for this function is the dataset we read from the JSON file.
•• This function will leverage the second function to tokenize each review in
the dataset.

The logic of this function is as follows:
1. Convert the input text string to lowercase.
2. Identify/replace punctuation with a space in the string.
3. Split the string into words based on spaces.
We can add this functionality with a new tokenize function that is shown in #7. This function should be added to the lib.py file.

# 7. A new tokenize function
import re
import json
def tokenize(text):
    if type(text) != str:
        raise Exception("Text must be a string")
    text_lower = text.lower()
    text_clean = re.sub("[^\w\s]", " ",text_lower)
    words = text_clean.split()
    return words

let’s consider the snippet of code in #3. This is not part of our main project, but rather a simple example using regular expressions.

# 8. Using a regular expression
import re
text = "Hello, Sean! -­ How are you?"
print(text)
text_clean = re.sub("[^\w]", " ",text)
print(text_clean)
words = text_clean.split()
print(words)

Tokenize an Input Review
------------------------
We also need a function that tokenizes a review, which means that the function will take a review as input (in the form of a dictionary), and then it will execute the tokenize function we just wrote on the key where the text is stored. To do this, add the code in #9 to the lib.py file.

# 9. The function to tokenize a review
def tokenize_review(review):
    if type(review) != dict:
        raise Exception("Review must be a dictionary")
    new_review = review.copy()
    words= tokenize(new_review[TEXT_KEY])
    new_review[WORDS_KEY] = words
    return new_review

We need to define the values TEXT_KEY and WORDS_KEY. At the top of lib.py, add the definitions as shown in #10.

# 10. Adding constants to the lib.py file
import re
import json
TEXT_KEY='reviewText'
WORDS_KEY = 'words'

Tokenize the Entire Dataset
----------------------------
The last step is to implement the code that will iterate through the entire dataset, tokenize each review, and store the words in an attribute. In order to do that, we will implement the tokenize_dataset function shown in #11.

# 11.Tokenizing the dataset
def tokenize_dataset(dataset):
    if type(dataset) != list:
        raise Exception("Dataset must be a list")
    result = list(map(tokenize_review, dataset))
    return result

Using the Tokenize Functions
-----------------------------
With the three functions now created to tokenize an input string, a review, and the entirecdataset, we are ready to see them in action using our reviews dataset. Start by updating the code in main.py as shown in #12.

# 12. Tokenizing our reviews dataset
from lib import *
dataset = read_json_file("/Users/haythembalti/Downloads/reviews.json")
print(dataset[0])
dataset_tokenized = tokenize_dataset(dataset)
print("Words of the first review:")
print(dataset_tokenized[0]['words'])
print("Words of the second review:")
print(dataset_tokenized[1]['words'])
print(type(dataset_tokenized))

Word Count for an Input List of Words
--------------------------------------
Again in lib.py, add the compute_word_count function shown in #13. Place it 
under the existing code.

# 13. The compute_word_count function
def compute_word_count(words):
    if type(words) != list:
        raise Exception("Words must be a list")
    word_count= dict()
    for word in words:
        if word in word_count:
            word_count[word] = word_count[word]+1
        else:
            word_count[word]=1
    return word_count

Word Count an Input Review
--------------------------
We use a separate compute_word_count_review function as shown in #14 to pull in the words from the review. Using the same logic as the tokenize_review, we are
building a word count function that will compute the word count of an input review (as dictionary).

# 14. compute_word_count_review
def compute_word_count_review(review):
    if type(review) != dict:
        raise Exception("Review must be a dictionary")
    new_review = review.copy()
    word_freq= compute_word_count(new_review[WORDS_KEY])
    new_review[WORD_COUNT_KEY] = word_freq
    return new_review

we use the WORD_COUNT_KEY as the variable where we store the key name
for the word count. WORD_COUNT_KEY needs to be added with the other constants at the top of lib.py, as indicated in # 15.

# 15.Current list of constants in lib.py
TEXT_KEY='reviewText'
WORDS_KEY = 'words'
WORD_COUNT_KEY = 'word_count'

Word Count for the Dataset
--------------------------
Similar to the tokenize functions, the last step is to implement the function that will compute the word count for the entire dataset. This function will take as input the dataset, iterate through it, and for each review, compute the word count. As with the tokenize function, we can do this by simply using the map function as shown in # 16.

# 16. The compute_word_count_dataset function
def compute_word_count_dataset(dataset):
    if type(dataset) != list:
        raise Exception("Dataset must be a list")
    result = list(map(compute_word_count_review, dataset))
    return result

In order to see everything in action, go back to main.py and add the code in #17 to the end of the file.

# 17. Updating main to count the words
dataset_word_count = compute_word_count_dataset(dataset_tokenized)
print("Word count for first review:")
print(dataset_word_count[0]['word_count'])
print("Word count for second review:")
print(dataset_word_count[1]['word_count'])

# 18. The completed lib.py file
import re
import json
TEXT_KEY='reviewText'
WORDS_KEY = 'words'
WORD_COUNT_KEY = 'word_count'

def read_json_file(path):
    if not path:
        raise Exception("You must provide a valid file path.")
    try:
        dataset = list()
        with open(path) as json_file:
            for line in json_file:
                dataset.append(json.loads(line))
        return dataset
    except (IOError, OSError):
        raise Exception("You must provide a valid JSON file.")

def compute_word_count(words):
    if type(words) != list:
        raise Exception("Words must be a list")
    word_count= dict()
    for word in words:
        if word in word_count:
            word_count[word] = word_count[word]+1
        else:
            word_count[word]=1
    return word_count

def compute_word_count_review(review):
    if type(review) != dict:
        raise Exception("Review must be a dictionary")
    new_review = review.copy()
    word_freq= compute_word_count(new_review[WORDS_KEY])
    new_review[WORD_COUNT_KEY] = word_freq
    return new_review
def compute_word_count_dataset(dataset):
    if type(dataset) != list:
        raise Exception("Dataset must be a list")
    result = list(map(compute_word_count_review, dataset))
    return result
def tokenize(text):
    if type(text) != str:
        raise Exception("Text must be a string")
    text_lower = text.lower()
    text_clean = re.sub("[^\w]", " ",text_lower)
    words = text_clean.split()
    return words
def tokenize_review(review):
    if type(review) != dict:
        raise Exception("Review must be a dictionary")
    new_review = review.copy()
    words= tokenize(new_review[TEXT_KEY])
    new_review[WORDS_KEY] = words
    return new_review
def tokenize_dataset(dataset):
    if type(dataset) != list:
        raise Exception("Dataset must be a list")
    result = list(map(tokenize_review, dataset))
    return result

# 19. The completed main.py file
from lib import *
#read dataset
dataset = read_json_file("reviews.json")
print(dataset[0])

#tokenize dataset
dataset_tokenized = tokenize_dataset(dataset)
print("Words of the first review:")
print(dataset_tokenized[0]['words'])
print("Words of the second review:")
print(dataset_tokenized[1]['words'])
print(type(dataset_tokenized))

#compute word count
dataset_word_count = compute_word_count_dataset(dataset_tokenized)
print("Word count for first review:")
print(dataset_word_count[0]['word_count'])
print("Word count for second review:")
print(dataset_word_count[1]['word_count'])
    