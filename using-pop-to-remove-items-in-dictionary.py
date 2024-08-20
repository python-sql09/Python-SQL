# 10.17 Using pop()
students_dict = dict()
students_dict['X10000'] = 'Michael'
students_dict['X10001'] = 'Nia'
students_dict['X10002'] = 'Anita'
print(students_dict)#print original dictionary
students_dict.pop("X10000")
print(students_dict)#we remove the first entry
#print modified dictionary
person = students_dict.pop("X10001") #remove and store an entry
print(person)
#we display the element returned from the pop method
print(students_dict) #print the final dictionary to see changes