from lib import *

# Read dataset
dataset = read_json_file("/home/linuxdeepa/python-sql09/Python-SQL/myprojects/Word-Analysis1/reviews.json")
print(f"Total reviews loaded: {len(dataset)}")

# Tokenize dataset
dataset_tokenized = tokenize_dataset(dataset)
print(f"Total reviews tokenized: {len(dataset_tokenized)}")

# Compute word count
dataset_word_count = compute_word_count_dataset(dataset_tokenized)

if dataset_tokenized:
    for i in range(min(6, len(dataset_tokenized))):  # Print details for the first 5 reviews or fewer
        review = dataset_tokenized[i]
        words = review['words']
        word_count = len(words)
        word_frequencies = compute_word_frequencies(words)
        
        print(f"Words of review {i + 1}: {words}")
        print(f"Word count of review {i + 1}: {word_count}")
        print(f"Word frequencies of review {i + 1}: {dict(word_frequencies)}")
else:
    print("No reviews were tokenized.")