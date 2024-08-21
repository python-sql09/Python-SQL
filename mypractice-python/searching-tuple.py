# 9.17 Searching a tuple
# create a tuple
tuple_of_names = ("Kate","Jennifer","Mike","Pete","Alex","Mike")
search_term = "Mike"
# check that the search term occurs at least once in the tuple
if search_term in tuple_of_names:
    print (search_term + " appears at least once in the tuple.")
# iterate through tuple to see if search term can be found
for name in tuple_of_names:
    if name == search_term:
        print("We found " + search_term)