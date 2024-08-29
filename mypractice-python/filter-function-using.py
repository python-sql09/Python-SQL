# 21.13 Using filter()
def initial_h(dataset):
    for x in dataset:
        if str.lower(x[0]) == "h": # normalize the case of the
            # first letter and look for 'h'
            return True
        else:
            return False
names=['Haythem','Mike','James','Helen','Mary']
print(names)
# extract the True results from the initial_h function to a new filter object
names_filtered = filter(initial_h,names)
print(type(names_filtered))
# convert the filter object to a list object
names_filtered_list = list(names_filtered)
print(type(names_filtered_list))
print(names_filtered_list)