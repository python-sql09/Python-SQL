# 10.19 Checking for the existence of a key
info = {
"name": "Robert",
"hobbies": ['fishing','dancing'],
"address": "123 Main Street, Louisville, KY"
}
key1 = "ssn"
if key1 in info.keys(): # we use the in operator to check if
    # the key1 exists in the list of keys
    print(key1 + " exists in the dictionary.")
    print("The value stored in the dictionary is: " + info[key1])
else:
    # display an error message if the key does not exist
    print(key1 + " does not exist in the dictionary.")
print("************************************************************")
key2 = "name"
if key2 in info.keys(): # we use the in operator to check if
    # the key2 exists in the list of keys
    print(key2 + " exists in the dictionary.")
    print("The value stored in the dictionary is: " + info[key2])
else:
    print(key2 + " does not exist in the dictionary.")