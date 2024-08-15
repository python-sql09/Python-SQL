# 8.6 Accessing the end of a list
list_of_strings = ["Kate", "Jennifer", "Mike", "Vedha"]
person_1 = list_of_strings[-1] #-1 refers to the last element in the list
print(person_1)
person_2 = list_of_strings[-2] #-2 refers to second-to-last element in list
print(person_2)
person_3 = list_of_strings[-3] #-3 refers to third-to-last element in list
print(person_3)
# this will report an error because there are only three items in the list
# I correct it
person_4 = list_of_strings[-4]
print(person_4)