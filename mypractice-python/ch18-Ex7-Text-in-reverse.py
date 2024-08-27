# Exercise 7: Text in Reverse
# Write a function that takes as input a text file and a new filename, and then copies the
# contents of the input text file to another file using the new filename. As a challenge,
# update the code so that the lines in the new file are in the reverse order of the lines in the
# original file.
def reverse_file_lines(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()
        
        # Reverse the order of the lines
        reversed_lines = lines[::-1]
        
        with open(output_file_path, 'w') as output_file:
            output_file.writelines(reversed_lines)
        
        print(f"Contents of {input_file_path} have been successfully reversed and written to {output_file_path}.")
    except FileNotFoundError:
        print("Input file not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
reverse_file_lines('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example.txt', '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/reversed_output.txt')