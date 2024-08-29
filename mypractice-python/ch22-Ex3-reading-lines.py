# Exercise 3: Reading Lines
# Write a function that prompts the reader for an integer n and reads the first n lines of a
# file. Include a creative way to handle cases where n is greater than the number of lines
# available in the file.
# Add exception handling for these cases:
# •• The user enters something other than an integer for n.
# •• The file cannot be located.
def read_lines_from_file(file_path):
    """Read the first n lines from a file and handle cases where n exceeds the number of lines."""
    try:
        # Prompt user for the number of lines to read
        n = int(input("Enter the number of lines to read from the file: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Handle cases where n is greater than the number of lines available
            if n > len(lines):
                print(f"The file only contains {len(lines)} lines. Displaying all available lines.")
                n = len(lines)
            # Display the first n lines
            print(f"Displaying the first {n} lines from the file:\n")
            for line in lines[:n]:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' cannot be found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'example.txt' with the path to your file
    read_lines_from_file('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example.txt')