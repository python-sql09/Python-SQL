# Adding constants to the lib.py file
import re
import json
from collections import Counter
# Current list of constants in lib.py
TEXT_KEY='reviewText'
WORDS_KEY = 'words'
WORD_COUNT_KEY = 'word_count'

# Adding exception handling to our function
def read_json_file(path):
    if not path:
        raise Exception("You must provide a valid file path.")
    try:
        with open(path, 'r') as json_file:
            dataset = json.load(json_file)  # Read the entire file content as JSON
    except (IOError, OSError):
        raise Exception("You must provide a valid JSON file.")
    except json.JSONDecodeError:
        raise Exception("The JSON file is not properly formatted.")
    return dataset

# The compute_word_count function
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

# compute_word_count_review
def compute_word_count_review(review):
    if type(review) != dict:
        raise Exception("Review must be a dictionary")
    new_review = review.copy()
    word_freq= compute_word_count(new_review[WORDS_KEY])
    new_review[WORD_COUNT_KEY] = word_freq
    return new_review

# The compute_word_count_dataset function
def compute_word_count_dataset(dataset):
    if type(dataset) != list:
        raise Exception("Dataset must be a list")
    result = list(map(compute_word_count_review, dataset))
    return result

# Tokenize function
def tokenize(text):
    if type(text) != str:
        raise Exception("Text must be a string")
    
    text_lower = text.lower()
    text_clean = re.sub(r"[^\w\s]", " ", text_lower)
    words = text_clean.split()
    return words

# Function to tokenize a review
def tokenize_review(review):
    if type(review) != dict:
        raise Exception("Review must be a dictionary")
    
    if TEXT_KEY not in review:
        return None  # Skip or handle missing key

    new_review = review.copy()
    words = tokenize(new_review[TEXT_KEY])
    new_review[WORDS_KEY] = words
    return new_review

# Function to tokenize the entire dataset
def tokenize_dataset(dataset):
    tokenized_reviews = []
    for review in dataset:
        if "comment" in review:  # Ensure that the key exists
            words = review["comment"].split()  # Simple tokenization by splitting on whitespace
            tokenized_reviews.append({"review_id": review["review_id"], "words": words})
        else:
            print(f"Review without 'comment': {review}")  # Debug print if 'comment' key is missing
    return tokenized_reviews

def compute_word_count_dataset(dataset_tokenized):
    word_counts = Counter()
    for review in dataset_tokenized:
        word_counts.update(review["words"])
    return word_counts

def compute_word_count(review):
    return len(review['words'])

def compute_word_frequencies(review):
    words_lower = [word.lower() for word in review['words']]
    return Counter(words_lower)