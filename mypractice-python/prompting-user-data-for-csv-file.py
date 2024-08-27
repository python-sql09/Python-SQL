# 19.10 Prompting the user for data for a CSV file
import csv
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/user_input.csv', 'w', newline='') as csv_file:
    while True:
        user_input = input("Please enter text to add to file [enter quit to exit]: ")
        if user_input.lower() == 'quit':
            break
        else:
            writer = csv.writer(csv_file,delimiter=',')
            writer.writerow([user_input])
f = open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/user_input.csv', 'r')
print(f.read())
f.close()