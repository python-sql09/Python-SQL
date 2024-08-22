# 13.10 Using keyword arguments
def my_function(fam1, fam2, fam3):
    print("The youngest family member is "+fam3)
my_function(fam1="Ezekiel",fam2="Sherry",fam3="Louis")
print("------")
my_function(fam2="Homer",fam3="Lisa",fam1="Bart")