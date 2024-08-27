# Exercise 5: Longest Word
# Write a function that takes as input the path to a text file and returns the longest word in
# the text file.
def find_longest_word(file_path):
    longest_word = ""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    # Remove punctuation from the word
                    clean_word = ''.join(char for char in word if char.isalnum())
                    if len(clean_word) > len(longest_word):
                        longest_word = clean_word
        return longest_word if longest_word else "No words found in the file."
    except FileNotFoundError:
        return "File not found. Please provide a valid file path."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
longest_word = find_longest_word('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example1.txt')
print(f"The longest word is: {longest_word}")