import re
import json
from collections import Counter

TEXT_KEY = 'text'
WORDS_KEY = 'words'
WORD_COUNT_KEY = 'word_count'

def read_json_file(path):
    if not path:
        raise Exception("You must provide a valid file path.")
    try:
        with open(path, 'r') as json_file:
            dataset = json.load(json_file)
        return dataset
    except (IOError, OSError, json.JSONDecodeError):
        raise Exception("You must provide a valid JSON file.")

def compute_word_frequencies(words):
    if not isinstance(words, list):
        raise Exception("Words must be a list")
    words_lower = [word.lower() for word in words]
    return Counter(words_lower)

def compute_word_count_review(review):
    if not isinstance(review, dict):
        raise Exception("Review must be a dictionary")
    new_review = review.copy()
    word_freq = compute_word_frequencies(new_review[WORDS_KEY])
    new_review[WORD_COUNT_KEY] = dict(word_freq)
    return new_review

def compute_word_count_dataset(dataset):
    if not isinstance(dataset, list):
        raise Exception("Dataset must be a list")
    return list(map(compute_word_count_review, dataset))

def tokenize(text):
    if not isinstance(text, str):
        raise Exception("Text must be a string")
    text_lower = text.lower()
    text_clean = re.sub(r"[^\w\s]", "", text_lower)
    words = text_clean.split()
    return words

def validate_data(dataset):
    for index, review in enumerate(dataset):
        if not isinstance(review, dict):
            raise ValueError(f"Review at index {index} is not a dictionary.")
        if 'comment' not in review:
            raise ValueError(f"Review at index {index} does not contain a 'comment' key.")

def tokenize_review(review):
    if not isinstance(review, dict):
        raise Exception("Review must be a dictionary")
    new_review = review.copy()
    words = tokenize(new_review['comment'])  # Use 'comment' key
    new_review[WORDS_KEY] = words
    return new_review

def tokenize_dataset(dataset):
    if not isinstance(dataset, list):
        raise Exception("Dataset must be a list")
    return list(map(tokenize_review, dataset))

def save_results(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)