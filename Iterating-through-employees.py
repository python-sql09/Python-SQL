# Iterating through employees
employees = ["Billy", "Jayden", "Magda", "Luis"]
for ctr in employees:
 # iterate through the list of employees
    print(ctr)
    for ctr2 in ctr:
    # iterate through each employee
        print(ctr2.upper())
    print("-­-­-­-­")

employees = ["Billy", "Jayden", "Magda", "Luis"]
for name in employees:
    print(name)
    for letter in name:
        print(letter.upper())
    print("----")

