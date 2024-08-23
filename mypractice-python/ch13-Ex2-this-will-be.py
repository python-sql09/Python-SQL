# Exercise 2: This Will Be
# Create a function that searches a string for an input group of characters and replaces each
# instance of the group with a new group of characters. For example, the function might be
# used to replace all occurrences of the phrase “this is” with “this will be.
# Define the function to replace a group of characters, case-insensitively
def replace_text_case_insensitive(original_text, search_group, replace_group):
    # Convert both the original_text and search_group to lowercase for matching
    lower_original = original_text.lower()
    lower_search = search_group.lower()
    
    # Perform the replacement using case-insensitive logic
    result_text = ""
    i = 0
    while i < len(lower_original):
        # Check if the current part of the text matches the search group
        if lower_original[i:i+len(lower_search)] == lower_search:
            result_text += replace_group
            i += len(lower_search)
        else:
            result_text += original_text[i]  # Keep the original case
            i += 1
    
    return result_text

# Example usage:
# Sample string
text = "This is an example. This is a simple task."

# Prompt user for the search group and replace group
search_group = input("Enter the group of characters to search for: ")
replace_group = input("Enter the group of characters to replace it with: ")

# Call the replace_text_case_insensitive function
updated_text = replace_text_case_insensitive(text, search_group, replace_group)

# Display the result
print("\nOriginal Text:")
print(text)
print("\nUpdated Text:")
print(updated_text)