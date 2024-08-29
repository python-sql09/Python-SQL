# Exercise 5: Creating a List from a File
# Write a function that reads a text file line by line, stores each line in a list, and then returns
# the list. Add exception handling for problems with the file.
def create_list_from_file(file_path):
    """Reads a text file line by line, stores each line in a list, and returns the list."""
    lines = []
    try:
        # Open the file and read line by line
        with open(file_path, 'r') as file:
            for line in file:
                lines.append(line.strip())  # Strip newline characters from each line
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' cannot be found.")
        return []
    except IOError:
        print(f"Error: An IOError occurred while reading '{file_path}'.")
        return []
    return lines

# Example usage
if __name__ == "__main__":
    # Replace this path with the path to your file
    file_path = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example2.txt'
    lines_list = create_list_from_file(file_path)
    if lines_list:
        print("File contents:")
        for line in lines_list:
            print(line)
    else:
        print("No lines were read from the file.")