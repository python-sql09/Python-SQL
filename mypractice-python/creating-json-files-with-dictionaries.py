# 20.1 Creating a JSON file from Python dictionaries
import json
# Create a list of dictionaries
data = []
data.append({"name":"Andre Richards","DOB":"10/10/1979"})
data.append({"name":"Melinda Jefferson","DOB":"12/31/1979"})
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/person.json', 'w') as outfile:
    json.dump(data, outfile)
# Print the file's contents
f = open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/person.json', 'r')
print(f.read())
f.close()