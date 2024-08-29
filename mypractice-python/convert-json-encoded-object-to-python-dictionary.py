# 20.4 Converting a JSON-encoded object to a Python dictionary
import json
json_dict = {
    "first_name": "Robert",
    "last_name": "Balti",
    "role": ["Manager", "Lead Developer"],
    "age": 34
}
# Convert a dictionary into a JSON formatted string object.
json_data = json.dumps(json_dict)
print(json_data)
print(type(json_data)) # string
# Convert a JSON encoded object into a python dictionary.
python_dict = json.loads(json_data)
print(python_dict)
print(type(python_dict)) # dict