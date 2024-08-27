# Exercise 6: Listing Text
# Write a function that takes as input a list of strings and writes the list to a text file. Each
# element in the list should be a separate line in the new text file.
def write_list_to_file(file_path, lines_list):
    try:
        with open(file_path, 'w') as file:
            for line in lines_list:
                file.write(line + '\n')
        print(f"List has been successfully written to {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
my_list = ["First line", "Second line", "Third line"]
write_list_to_file('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/output1.txt', my_list)