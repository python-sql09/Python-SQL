# 20.9 Using pprint
import json
from pprint import pprint
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/prize.json','r') as jsonfile:
    data = json.load(jsonfile) # load the json content and serialize it.
print(type(data)) #dict
pprint(data)
# print the entire file content.