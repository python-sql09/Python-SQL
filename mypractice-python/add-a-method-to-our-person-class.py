# 14.3 Adding a method to our Person class
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    def display_info(self):
        print("Person First Name: " + self.first_name)
        print("Person Last Name: " + self.last_name)
person_1 = Person("Lewis","Montes")
person_1.display_info()
person_2 = Person("Robin","Durham")
person_2.display_info()