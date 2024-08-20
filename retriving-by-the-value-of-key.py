# 10.15 Retrieving by the value of the key
info = {
"name": "Robert",
"age": 34,
"address": "123 Main Street, Louisville, KY"
}
name = info.get("name") # access the value of the key name directly.
print(name)