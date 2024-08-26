# 18.8 Creating a function to read lines of a file
def head(filepath,num_lines):
    f = open(filepath, mode="r")
    lines = ""
    for x in range(num_lines):
        lines += f.readline()
    f.close()
    return lines
# return the first 3 lines in the file
text = head("data/incidentticket.txt",3)
print(text)