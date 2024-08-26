#18.3 Reading the contents of a text file
f = open("data/open-flat1and01-file.txt", mode="r")
text = f.read()
print(text)
f.close()