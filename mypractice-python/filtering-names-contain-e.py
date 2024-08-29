# 21.14 Filtering for names containing an “e”
def contains_e(dataset):
    if 'e' in dataset:
        return True
    else:
        return False
names=['Haythem','Mike','James','Helen','Mary']
print(names)
names_filtered = filter(contains_e,names)
print(type(names_filtered))
names_filtered_list = list(names_filtered)
print(type(names_filtered_list))
print(names_filtered_list)