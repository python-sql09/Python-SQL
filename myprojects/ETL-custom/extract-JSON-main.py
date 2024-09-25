from extract import extract
e = extract()
dataset = e.fromJSON(file_path = "person.json")
print(dataset)
print(len(dataset))