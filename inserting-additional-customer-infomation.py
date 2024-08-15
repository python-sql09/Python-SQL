# 8.15 Inserting additional customer information
info = ["John", "Smith", "Boston", "Junior Software Developer"]
info.insert(2, input("Please enter an address: "))
info.insert(3, input("Please enter a phone number: "))
#this code should be executed last
print("First name: " + info[0])
print("Last name: " + info[1])
print("Address: " + info[2])
print("Phone number: " + info[3])
print("City: " + info[4])
print("Profession: " + info[5])