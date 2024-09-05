from extract import extract
e = extract()
dataset = e.fromCSV(file_path="got_chars.csv")
for row in dataset:
    print(row)
