# 15.5 Overriding the display method
class Person:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
    def display(self):
        print("Person First Name: " + self.first_name)
        print("Person Last Name: " + self.last_name)
class Employee(Person):
    def display(self):
        print("Employee ID: " + self.employee_id)
        print("Employee First Name: " + self.first_name)
        print("Employee Last Name: " + self.last_name)
ourEmployee = Employee("Haythem","Balti")
ourEmployee.employee_id = "E15454513"
ourEmployee.display()