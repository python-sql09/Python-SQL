# 18.5 Creating a function to read characters from a file
def head(filepath,num_char):
    f = open(filepath, mode="r")
    output = f.read(num_char)
    f.close()
    return output
# return the first 20 characters in the file data/text.txt
text = head("data/incidentticket.txt",21)
print(text)