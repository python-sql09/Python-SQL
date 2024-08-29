# 20.2 Creating a JSON file with unstructured data
import json
json_dict = {
    "first_name": "Robert",
    "last_name": "Balti",
    "role": ["Manager", "Lead Developer"],
    "age": 34
}
# convert a dictionary into a string object that we can display.
json_data = json.dumps(json_dict)
print(json_dict)
# dict
print(type(json_dict))
print(json_data)
# string
print(type(json_data))