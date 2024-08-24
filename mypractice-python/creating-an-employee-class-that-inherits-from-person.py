# 15.2 Creating an Employee class that inherits from Person
# Create Person class
class Person:
# This is a parent or base class
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
    def display(self):
        print(self.first_name + " " + self.last_name)
# Create employee class that inherits from person class.
class Employee(Person):
# Employee is a child class
    pass
e = Employee("Haythem","Balti")
e.display()