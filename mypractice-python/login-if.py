# Using an if statement in Python
password = "admIn"
condition = (password == "admin")
# if condition is equal to True, which means the password is correct.
if condition:
    print("password correct")
#if condition is equal to False, which means the password is not correct.
if condition == False:
    print("password incorrect")

#Checking a username
correct_username="admin"
guessed_username = "Admin"
if correct_username == guessed_username:
#This will only display if the guessed username is equal
# to the correct username
    print("Access Granted")
else:
#This will only display if the guessed username is not equal
# to the correct username
    print("Access Denied")

