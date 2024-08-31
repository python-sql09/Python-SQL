# To handle and fix 27,000 JSON objects, especially if they are not properly 
# formatted or have parsing issues, you can automate the process using Python.

import json

# Step 1: Load the raw data
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/reviews.json', 'r') as file:
    raw_data = file.read()

# Step 2: Split the data into individual JSON objects
# The split assumes the JSON objects are not in a list and separated by a newline
raw_objects = raw_data.strip().split('\n')

# Step 3: Process and fix each JSON object
json_objects = []
for obj in raw_objects:
    try:
        # Attempt to parse each object
        json_object = json.loads(obj)
        json_objects.append(json_object)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON object: {e}")

# Step 4: Save the corrected JSON objects into a properly formatted list
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/corrected_data.json', 'w') as file:
    json.dump(json_objects, file, indent=4)

print(f"Successfully processed {len(json_objects)} JSON objects.")