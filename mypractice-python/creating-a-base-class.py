# 15.1 Creating a base class
class Person:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
    def display(self):
        print(self.first_name + " " + self.last_name)
x = Person("Asia", "Roberson")
x.display()