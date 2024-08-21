# 9.8 Slicing a tuple
info = ("Jonathan", "Vance", "679 Birchpond Street","Merrillville", "IN", "46410")
# we extract only the first two elements from the tuple and
# store them in a new tuple
name = info[0:2]
print("The name is:")
print(name)
# we extract only the last four elements from the tuple and
# store them in a new tuple
address = info[2:6]
print("The address is:")
print(address)