# 9.4 Password length
password = ('P', 'a', 's', 's', 'w', 'o', 'r', 'd')
if len(password) >= 8:
    print("Your password meets the requirements and the length is", len(password))
else:
    print("Your password length does not meet the requirements.")

password = input("Please enter the password minimum 8 characters: ")
if len(password) >= 8:
    print("Your password meets the requirements and the length is", len(password))
else:
    print("Your password length does not meet the requirements.")