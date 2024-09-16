from extract import extract
e = extract()
dataset = e.fromCSV(file_path="got_chars.csv")
for row in dataset:
    print(row)

'''# Example usage
e = Extract()
dataset = e.fromMONGODB(host="localhost", port=27017, username="mongodb", password="Deepa@369", db="amazon_records", collection="musical_instruments")
if dataset:
    print(len(dataset))
    print(dataset[0])'''