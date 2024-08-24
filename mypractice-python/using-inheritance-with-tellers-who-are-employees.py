# 15.3 Using inheritance with tellers who are employees
class Employee:
    def __init__(self,name_in,loc):
        self.name = name_in
        self.location = loc
    def display(self):
        print("Employee name: " + self.name)
        print("Employee location: " + self.location)
class Teller(Employee):
    pass
t1 = Teller("Regina Hayden","Baltimore")
t2 = Teller("Sonny Gutierrez","Philadelphia")
t1.display()
t2.display()