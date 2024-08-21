# 11.11 Checking the length of a set
user_names = set()
integer = int(input("Please enter an integer for the number of usernames you would like to enter: "))
while len(user_names) < integer:
    username = {input("Please enter a username: ")}
    user_names.update(username)
print(user_names)