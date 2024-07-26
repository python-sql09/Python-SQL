#When were you born (without error)?
year_born = input("Enter the year you were born: ")
current_year = input("Enter the current year: ")
# convert the strings into integers
born_int = int(year_born)
current_int = int(current_year)
age = current_int - born_int
print("Your age is:", age)