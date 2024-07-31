# Exercise 5: Company Picnic
# Ask the user for their last name
last_name = input("What's your last name? ").strip().capitalize()
# Get the first letter of the last name
first_letter = last_name[0]
# Determine the team based on the first letter
if first_letter in "ABCD":
    team = "Red Dragons"
elif first_letter in "EFGH":
    team = "Dark Wizards"
elif first_letter in "IJKL":
    team = "Moving Castles"
elif first_letter in "MNOP":
    team = "Golden Snitches"
elif first_letter in "QRST":
    team = "Night Guards"
elif first_letter in "UVWXYZ":
    team = "Black Holes"
else:
    team = "Unknown Team"
# Display the team assignment
print(f"Aha! You're on the team '{team}'!")
print("Good luck in the games!")
