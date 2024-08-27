# Exercise 1: Reading Lines
# Write a function that prompts the reader for an integer n and reads the first n lines of a
# file. Include a creative way to handle cases where n is greater than the number of lines
# available in the file.
def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if n > len(lines):
                print(f"The file only has {len(lines)} lines. Displaying all available lines:")
                n = len(lines)
            for i in range(n):
                print(f"Line {i + 1}: {lines[i].strip()}")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
read_first_n_lines('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example1.txt', 10)