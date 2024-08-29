# Exercise 4: Concatenating Files
# Write a function that takes as input the path to two text files and concatenates the files
# into a single new file. Include exception handling for problems with one or both input files.
def concatenate_files(file1_path, file2_path, output_path):
    """Concatenate the contents of two files into a new file."""
    try:
        # Open and read the first file
        with open(file1_path, 'r') as file1:
            content1 = file1.read()
    except FileNotFoundError:
        print(f"Error: The file '{file1_path}' cannot be found.")
        return
    except IOError:
        print(f"Error: An IOError occurred while reading '{file1_path}'.")
        return
    try:
        # Open and read the second file
        with open(file2_path, 'r') as file2:
            content2 = file2.read()
    except FileNotFoundError:
        print(f"Error: The file '{file2_path}' cannot be found.")
        return
    except IOError:
        print(f"Error: An IOError occurred while reading '{file2_path}'.")
        return
    try:
        # Write the concatenated content to the output file
        with open(output_path, 'w') as output_file:
            output_file.write(content1 + "\n" + content2)
        print(f"Files have been successfully concatenated into '{output_path}'.")
    except IOError:
        print(f"Error: An IOError occurred while writing to '{output_path}'.")

# Example usage
if __name__ == "__main__":
    # Replace these paths with the paths to your files
    file1 = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example.txt'
    file2 = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example1.txt'
    output_file = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/concatenated_output.txt'
    concatenate_files(file1, file2, output_file)