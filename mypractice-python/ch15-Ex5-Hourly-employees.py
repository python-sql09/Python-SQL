# Exercise 5: Hourly Employees
# Person class
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def display(self):
        print("Person First Name: " + self.first_name)
        print("Person Last Name: " + self.last_name)

# Employee class inheriting from Person
class Employee(Person):
    def __init__(self, emp_id, fname, lname):
        super().__init__(fname, lname)
        self.employee_id = emp_id

    def display(self):
        print("Employee ID: " + self.employee_id)
        print("Employee First Name: " + self.first_name)
        print("Employee Last Name: " + self.last_name)

# Director class inheriting from Employee
class Director(Employee):
    def __init__(self, emp_id, fname, lname, d_level):
        # Call Employee constructor
        super().__init__(emp_id, fname, lname)
        self.director_level = d_level
        self.team = []  # Team is a list of Employee objects

    def add_employee(self, emp):
        # Add an Employee object to the team
        self.team.append(emp)

    def display(self):
        # Display Director's info
        print("Director ID: " + self.employee_id)
        print("Director First Name: " + self.first_name)
        print("Director Last Name: " + self.last_name)
        print("Director Level: " + self.director_level)
        print("Team Members:")
        # Display info of each employee in the team
        for emp in self.team:
            emp.display()
            print("-----")

# HourlyEmployee class inheriting from Employee
class HourlyEmployee(Employee):
    def __init__(self, emp_id, fname, lname, hourly_rate=15.0):
        # Call Employee constructor
        super().__init__(emp_id, fname, lname)
        self.hourly_rate = hourly_rate

    def display(self):
        # Display HourlyEmployee's info
        print("Hourly Employee ID: " + self.employee_id)
        print("Hourly Employee First Name: " + self.first_name)
        print("Hourly Employee Last Name: " + self.last_name)
        print(f"Hourly Rate: ${self.hourly_rate}/hour")

# Create Director object
d1 = Director("E24523525", "Haythem", "Balti", "D-LEVEL-1")

# Create Employee object
e1 = Employee("E4746456456", "Mark", "Smith")
# Add employee e1 to the Director's team
d1.add_employee(e1)

# Create HourlyEmployee object
e2 = HourlyEmployee("E47464578978", "Mary", "Lang", hourly_rate=20.0)
# Add hourly employee e2 to the Director's team
d1.add_employee(e2)

# Display Director's info and team members
d1.display()