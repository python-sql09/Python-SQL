# 18.15 Prompting the user for a file to overwrite
input_1 = input("Please enter a file name: ")
input_2 = input("Enter the text you would like within the file: ")
f = open(input_1, mode="w")
f. write(input_2)
f.close()