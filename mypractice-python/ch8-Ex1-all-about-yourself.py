# Exercise 1: All About You
# Prompt the user to answer a series of 3–5 questions about themselves (such as their name,
# their age, their birthday, or where they live) and save the answers in a list. Display the
# results to the user.
# list to store user's answers
user_info = []
#Ask questions
name = input("What is your name? ")
user_info.append(name)
age = int(input("How old are you? "))
user_info.append(age)
dob=input("What is your date of birth (dd/mm/yyyy)?")
user_info.append(dob)
location1 = input("Where do you born? ")
user_info.append(location1)
location2 = input("Where do you live? ")
user_info.append(location2)
location3 = input("Where do you work? ")
user_info.append(location3)
print("\n User Information: ")
for info in user_info:
    print(info)

