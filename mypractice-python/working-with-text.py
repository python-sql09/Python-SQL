import string

def get_unique_words(filename):
    # Create an empty dictionary to store unique words
    word_dict = {}
    
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read each line in the file
            for line in file:
                # Remove punctuation and convert to lowercase
                words = line.translate(str.maketrans('', '', string.punctuation)).lower().split()
                
                # Add each word to the dictionary
                for word in words:
                    if word not in word_dict:
                        word_dict[word] = 1  # Add word to the dictionary
                    # For uniqueness, we don't increment the count
                
        # Sort the dictionary by the keys (words)
        sorted_words = dict(sorted(word_dict.items()))
        
        # Print the sorted dictionary
        for word in sorted_words:
            print(word)
    
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

# Example usage
filename = input("Enter the filename (with extension): ")
get_unique_words(filename)