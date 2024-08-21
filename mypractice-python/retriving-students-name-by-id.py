# 10.9 Retrieving student names by ID
students_dict = dict()
students_dict['X10000'] = 'Michael'
students_dict['X10002'] = 'Nia'
students_dict['X10001'] = 'Anita'
for student_id in students_dict.keys():
    print(students_dict[student_id])