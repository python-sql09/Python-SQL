# 13.12 The display function
def display(**kwargs):
    # iterate through the list…
    for keyword,value in kwargs.items():
        print(keyword + ": " + value)
display(first_name = 'Robert', last_name = 'Johnson')
print("------")
display(first_name = 'Mary', age = "32", location = "Dallas")