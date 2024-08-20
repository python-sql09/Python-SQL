# 10.11 Retrieving keys and values
students_dict = dict()
students_dict['X10000'] = 'Michael'
students_dict['X10002'] = 'Nia'
students_dict['X10001'] = 'Anita'
for key,value in students_dict.items():
    print(key)
    print(value)