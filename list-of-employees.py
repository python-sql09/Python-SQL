# A list of employees
list1 = []
num = input ("Enter number: ")
print(num)
for num in range(0,int(num)):
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    position = input("Enter position: ")
    empnum = input("Enter employee number: ")
    list_of_items = [firstname, lastname, position, empnum]
    list1.append(list_of_items)
for ctr in list1:
    print(*ctr, sep = ", ")
