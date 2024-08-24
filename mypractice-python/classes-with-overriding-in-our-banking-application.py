# 15.6 Classes with overriding in our banking application
class Employee:
    def __init__(self,n,i):
        self.name=n
        self.id=i
    def display(self):
        print("Employee name is: " + self.name)
        print("Employee ID is: " + self.id)
class Manager(Employee):
    def __init__(self,t,n,i):
        Employee.__init__(self,n,i)
        self.team=t
        self.id=i
    def display(self):
        print("Manager's employee ID is: " + self.id)
        print("Manager's name is: " + self.name)
        print("Manager's team is: " + self.team)
m1=Manager("Robert A, LaTerrance S","Julia Juarez","A1152254")
m2=Manager("Lilyana J, Angeline P","Whitney Solomon","A1155626")
m1.display()
m2.display()
class Teller(Employee):
    def __init__(self,b,n,i):
        Employee.__init__(self,n,i)
        self.bank_branch=b
    def display(self):
        print("Teller's employee ID is: " + self.id)
        print("Teller's name is: " + self.name)
        print("Teller's bank branch is: " + self.bank_branch)
t1=Teller("Columbia Ave.","Lamar Mercer","A1152278")
t2=Teller("Constitution Dr.","Karly Robinson","A1152278")
t1.display()
t2.display()
class CustomerServRep(Employee):
    def __init__(self,c,n,i):
        Employee.__init__(self,n,i)
        self.call_center=c
    def display(self):
        print("Customer Service Rep's employee ID is: " + self.id)
        print("Customer Service Rep's name is: " + self.name)
        print("Customer Service Rep's call center is: " + self.call_center)
cs1=CustomerServRep("Headquarters","Clayton Ryan","A1152211")
cs2=CustomerServRep("Headquarters","Gage Barnett","A1152212")
cs1.display()
cs2.display()