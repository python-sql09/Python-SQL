# 10.13 Seeing the different method output
# •• keys() returns a collection of each individual key in the dictionary.
# •• values() returns a collection of each of the values in the dictionary.
# •• items() returns a collection with each of the key: value pairs in the dictionary.
students_dict = dict()
students_dict['X10000'] = 'Michael'
students_dict['X10002'] = 'Nia'
students_dict['X10001'] = 'Anita'
print(students_dict.keys())
print(students_dict.values())
print(students_dict.items())