# 15.4 Multiple levels of inheritance
class Person:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
    def display(self):
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
class Employee(Person):
    def __init__(self,emp_id,fname,lname):
        Person.__init__(self,fname,lname)
        self.employee_id =emp_id
class Director(Employee):
    def __init__(self,emp_id,fname,lname,d_level):
        Employee.__init__(self,emp_id,fname,lname)
        self.director_level = d_level
d1 = Director("E24523525","Haythem","Balti","D-LEVEL-1")
d1.display()
print("Employee ID: " + d1.employee_id)
print("Director Level: " + str(d1.director_level))
print("------")
d2 = Director("E425345324534","Haythem","Balti","D-LEVEL-5")
d2.display()
print("Employee ID: " + d2.employee_id)
print("Director Level: " + str(d2.director_level))