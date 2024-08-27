# Exercise 3: Combination of Them All
# Write a function that takes a variable number of text files and concatenates them into a
# single new file.
def concatenate_multiple_files(output_file_path, *file_paths):
    try:
        with open(output_file_path, 'w') as output_file:
            for index, file_path in enumerate(file_paths, start=1):
                try:
                    with open(file_path, 'r') as input_file:
                        output_file.write(input_file.read())
                        if index < len(file_paths):
                            output_file.write(f"\n--- End of File {index} ({file_path}) ---\n\n")
                except FileNotFoundError:
                    print(f"File not found: {file_path}. Skipping this file.")
                except Exception as e:
                    print(f"An error occurred while processing {file_path}: {e}")
        print(f"All provided files have been successfully concatenated into {output_file_path}.")
    except Exception as e:
        print(f"An error occurred while creating the output file: {e}")

# Example usage:
concatenate_multiple_files('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/output.txt', '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example.txt', '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example1.txt', '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example2.txt')