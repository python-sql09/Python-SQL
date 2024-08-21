# 10.25 Updating a referenced dictionary
students_dict = dict()
students_dict['X10000'] = 'Michael'
students_dict['X10001'] = 'Nia'
students_dict['X10002'] = 'Anita'
students_dict2 = students_dict
print(students_dict)
print(students_dict2)
update_person = {'X10002':'Beth'}
new_person = {'X10003':'George'}
new_person1 = {'X10004':'Sri'}
new_person2 = {'X10005':'Shelly'}
new_person3 = {'X10006':'Selvi'}
students_dict.update(update_person)
students_dict.update(new_person)
students_dict.update(new_person1)
students_dict.update(new_person2)
students_dict.update(new_person3)
print(students_dict)
print(students_dict2)