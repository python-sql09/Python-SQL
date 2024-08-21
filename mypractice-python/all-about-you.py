# Create an empty list to store the user's answers
user_info = []

# Prompt the user with a series of questions
name = input("What is your name? ")
age = input("How old are you? ")
birthday = input("When is your birthday? ")
city = input("Where do you live? ")
hobby = input("What is your favorite hobby? ")

# Save the answers in the list
user_info.append(name)
user_info.append(age)
user_info.append(birthday)
user_info.append(city)
user_info.append(hobby)

# Display the results to the user
print("\nHere is the information you provided:")
print(f"Name: {user_info[0]}")
print(f"Age: {user_info[1]}")
print(f"Birthday: {user_info[2]}")
print(f"City: {user_info[3]}")
print(f"Favorite Hobby: {user_info[4]}")