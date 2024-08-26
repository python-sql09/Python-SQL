# 18.7 Reading lines of a text file
f = open("data/incidentticket.txt", "r") # read file in read mode.
print(f.readline()) # read first line
print(f.readline()) # read second line
print(f.readline()) # read third line
print(f.readline()) # read fourth line
f.close()