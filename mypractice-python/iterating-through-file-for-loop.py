# 18.9 Iterating through a file
f = open("data/incidentticket.txt", "r")
for line in f: # the file object can be iterated on at the line level.
    print(line) # with each iteration, line contains the current line.
f.close()