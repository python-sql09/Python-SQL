# Exercise 2: Combination of the Two
# Write a function that takes as input the path to two text files and concatenates the files
# into a single new file.
def concatenate_files(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_file_path, 'w') as output_file:
            # Read and write content from the first file
            output_file.write(file1.read())
            # Optionally add a separator between the two files
            output_file.write("\n--- End of File 1 ---\n\n")
            # Read and write content from the second file
            output_file.write(file2.read())
        print(f"Files have been successfully concatenated into {output_file_path}.")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}. Please provide valid file paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
concatenate_files('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example.txt', '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example1.txt', '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/output.txt')
