from lib import (
    read_json_file,
    tokenize_dataset,
    compute_word_count_dataset,
    save_results,
    validate_data,
    compute_word_frequencies
)
from visualization import visualize_word_frequencies
from collections import Counter  # Add this line
# Read dataset
dataset = read_json_file("/home/linuxdeepa/python-sql09/Python-SQL/myprojects/Word-Analysis2/reviews.json")
print(f"Total reviews loaded: {len(dataset)}")

# Validate dataset
validate_data(dataset)

# Tokenize dataset
dataset_tokenized = tokenize_dataset(dataset)
print(f"Total reviews tokenized: {len(dataset_tokenized)}")

# Compute word count
dataset_word_count = compute_word_count_dataset(dataset_tokenized)

# Collect all word frequencies
all_word_frequencies = Counter()
for review in dataset_tokenized:
    words = review['words']
    all_word_frequencies.update(compute_word_frequencies(words))

# Save results
save_results(dataset_word_count, "/home/linuxdeepa/python-sql09/Python-SQL/myprojects/Word-Analysis2/word_counts.json")

# Visualize word frequencies (only once for all reviews)
visualize_word_frequencies(all_word_frequencies)

# Print the first few items in the dataset to inspect its structure
print("Sample of loaded dataset:")
print(dataset[:5])  # Print the first 5 items