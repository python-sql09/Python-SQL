# LISTING 20.3 Formatting our output with indent
import json
json_dict = {
    "first_name": "Robert",
    "last_name": "Balti",
    "role": ["Manager", "Lead Developer"],
    "age": 34
}
json_data = json.dumps(json_dict,indent = 3)
print(json_data)
print(type(json_data))
json_data = json.dumps(json_dict,indent = 9)
print(json_data)
