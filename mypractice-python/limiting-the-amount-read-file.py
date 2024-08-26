# 18.4 Limiting the amount read
f = open("data/open-flat1and01-file.txt", "r")
print(f.read(100)) # this will pull the first 100 characters
f.close()