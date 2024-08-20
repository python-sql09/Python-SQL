# 10.21 Updating a dictionary
students_dict = dict()
students_dict['X10000'] = 'Michael'
students_dict['X10001'] = 'Nia'
students_dict['X10002'] = 'Anita'
print(students_dict)
new_person = {'X10000':'Jeffrey'} # create a new entry (key: value pair)
students_dict.update(new_person) # use the update method to update the value
# for key 'X10000'
print(students_dict)
new_person = {'X10003':'Erin'}
students_dict.update(new_person)
print(students_dict)