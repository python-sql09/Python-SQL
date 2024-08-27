# 18.17 Prompting the user to create a file
input_1 = input("Please enter a file name: ")
input_2 = input("Enter the text you would like within the file: ")
input_3 = input("Enter the read/write mode for the file [a,x,r,w]: ")
f = open(input_1, input_3)
f. write(input_2)
f.close()