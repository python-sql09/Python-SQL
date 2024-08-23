# 14.2 Person class with multiple attributes
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
person_1 = Person("Lewis", "Montes")
print(person_1.first_name)
print(person_1.last_name)
person_2 = Person("Robin", "Durham")
print(person_2.first_name)
print(person_2.last_name)