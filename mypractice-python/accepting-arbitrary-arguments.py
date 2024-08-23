# 13.11 Accepting arbitrary arguments
def my_function(**family):
    print("Her last name is " + family["lname"])
my_function(fname = "Emery", lname = "McMillan")