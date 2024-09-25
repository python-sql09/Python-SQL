from extract import extract
e = extract()
query = "SELECT * FROM artist;"
dataset = e.fromMYSQL(
    host="localhost",
    username="root",
    password="Deepa@369",
    db="deeparecordshop",
    query=query
)

print(dataset)
print(len(dataset))