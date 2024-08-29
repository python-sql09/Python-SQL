# Exercise 2: Converting a Text File to Uppercase
# Create a script that uses the map() function to convert the contents of a text file into
# uppercase.
# Function to convert text file contents to uppercase
def convert_file_to_uppercase(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile:
        lines = infile.readlines()

    # Convert each line to uppercase using map
    uppercase_lines = list(map(str.upper, lines))

    # Write the uppercase lines to a new file
    with open(output_file_path, 'w') as outfile:
        outfile.writelines(uppercase_lines)

# Example usage
input_file = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/input3.txt'      # Replace with the path to your input file
output_file = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/output3.txt'    # Replace with the desired path for the output file
convert_file_to_uppercase(input_file, output_file)

print(f"The contents of {input_file} have been converted to uppercase and saved in {output_file}.")