# Exercise 5: Which Is Greater?
def compute_max_value(**kwargs):
    # Initialize variables to store the word with the highest value
    max_word = None
    max_value = float('-inf')  # Start with the smallest possible number
    # Iterate over each word and its corresponding value
    for word, value in kwargs.items():
        # Update the max_word and max_value if the current value is greater
        if value > max_value:
            max_word = word
            max_value = value
    # Return the word with the highest value as a tuple (word, value)
    return max_word, max_value
# Test the function
(word, freq) = compute_max_value(word_1=1, word_2=3, word_3=6, word_4=5)
print(word, freq)  # should return word_3 6