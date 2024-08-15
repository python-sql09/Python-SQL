#8.5 Accessing names by index
list_of_strings = ["Kate", "Jennifer", "Mike", "Vedha"]
print(list_of_strings)
#access the first element in the list using the [] and
#the index starting from zero for the first element
person_1 = list_of_strings[0] #access the first element of the list
print(person_1)
person_2 = list_of_strings[1] #access the second element of the list
print(person_2)
person_3 = list_of_strings[2] #access the third (and last) element of the list
print(person_3)
#this will cause an error because there are only three items in the list
# I add one more person to prevent error
person_4 = list_of_strings[3]
print(person_4)