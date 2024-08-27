import os

script_dir = os.path.dirname(__file__)  # Get the script's directory
file_path = os.path.join(script_dir, "data/working-with-text.txt")  # Construct the full path

with open(file_path, "r") as file:
    content = file.read()
    print(content)