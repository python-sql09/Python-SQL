# listing 14.5 Classes to represent employees in our banking app
class Manager():
    def __init__(self, n, i, t):
        self.name = n
        self.id = i
        self.team = t
    def display(self):
        print("Manager name is: " + self.name)
        print("Manager ID is: " + self.id)
        print("Manager's team is: ")
        for member in self.team:
            print(member)

class Teller():
    def __init__(self, n, i, b):
        self.name = n
        self.id = i
        self.bank_branch = b
    def display(self):
        print("Teller's employee ID is:" + self.id)
        print("Teller's name is: " + self.name)
        print("Teller's bank branch is: " + self.bank_branch)

class CustomerServRep():
    def __init__(self, n, i, c):
        self.name = n
        self.id = i
        self.call_center = c
    def display(self):
        print("Customer Service Rep's employee ID is:" + self.id)
        print("Customer Service Rep's name is: " + self.name)
        print("Customer Service Rep's call center is: " + self.call_center)

# Create managers
m1 = Manager("Julia Juarez", "A1152254", ["Robert A", "LaTerrance S"])
m2 = Manager("Whitney Solomon", "A1155626",["Lilyana J", "Angeline P"])
m1.display()
m2.display()
# Create tellers
t1 = Teller("Lamar Mercer", "A1152278", "Columbia Ave.")
t2 = Teller("Karly Robinson", "A1152278", "Constitution Dr.")
t1.display()
t2.display()
# Create Customer Service Reps
cs1 = CustomerServRep("Clayton Ryan", "A1152211", "Headquarters")
cs2 = CustomerServRep("Gage Barnett", "A1152212", "Headquarters")
cs1.display()
cs2.display()