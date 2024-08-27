# Exercise 4: Listing Lines
# Write a function that reads a text file line by line, stores each line in a list, and then
# returns the list
def list_lines_from_file(file_path):
    lines_list = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines_list.append(line.strip())
        return lines_list
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
lines = list_lines_from_file('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example.txt')
print(lines)