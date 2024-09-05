# 3 The fromJSON method
class extract:
    def fromJSON(self, file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset

e = extract()
dataset = e.fromJSON(file_path = "/home/linuxdeepa/python-sql09/Python-SQL/myprojects/ETL-scripting/person.json")
print(dataset)
print(len(dataset))