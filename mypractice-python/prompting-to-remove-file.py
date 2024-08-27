# 18.21 Prompting to remove a file
import os
file_name = input("Please enter a file name to check for: ")
directory = "/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/"
if os.path.exists(directory+file_name):
    print("The file exists.")
    user_input = input("Would you like to delete the file? [yes/no]")
    if user_input.lower() == 'yes':
        os.remove(directory+file_name)
        print("The file "+directory+file_name+" was deleted successfully.")
    print("File Not Deleted")
else:
    print("The file doesn't exist.")