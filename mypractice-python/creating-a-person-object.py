# 14.1 Creating a Person object
class Person:
    # init method or constructor
    def __init__(self, name):
        self.name = name #name is an instance attribute.
p = Person("Karl Johnson")
print(p.name)