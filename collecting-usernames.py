# Collecting usernames
names = []
uContinue = ""
while uContinue != "N":
    name = input("What's your name? ")
    print("You entered: "+name)
    names.append(name)
    uContinue = input("Continue (Y or N) ")
print(names)
