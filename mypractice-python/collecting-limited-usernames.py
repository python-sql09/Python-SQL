# Collecting a limited number of usernames
names = []
uContinue = ""
count = 0
while count < 5 and uContinue != "N":
    name = input("What's your name? ")
    print("You entered: "+name)
    count += 1
    names.append(name)
    uContinue = input("Continue (Y or N) ")
print(names)
