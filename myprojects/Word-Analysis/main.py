# Word Analysis in Python
#--------------------------
from lib import *

dataset = read_json_file("/home/linuxdeepa/python-sql09/Python-SQL/myprojects/Word-Analysis/reviews.json")
print(f"Total reviews loaded: {len(dataset)}")

dataset_tokenized = tokenize_dataset(dataset)
print(f"Total reviews tokenized: {len(dataset_tokenized)}")

if dataset_tokenized:
    for i in range(min(6, len(dataset_tokenized))):  # Print details for the first 5 reviews or fewer
        review = dataset_tokenized[i]
        words = review['words']
        word_count = len(words)
        word_frequencies = compute_word_frequencies(review)
        
        print(f"Words of review {i + 1}: {words}")
        print(f"Word count of review {i + 1}: {word_count}")
        print(f"Word frequencies of review {i + 1}: {dict(word_frequencies)}")
else:
    print("No reviews were tokenized.")
    





