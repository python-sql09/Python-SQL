# 21.9 Converting a characters to uppercase
def to_upper_case(s):
    return str(s).upper()

names=['haythem','mike','james']
print(names)

names_upper = map(to_upper_case, names) # apply to_upper_case function to each element in names
print(type(names_upper))
names_upper_list = list(names_upper) # convert the names_upper map object to a
				
# python list.
print(names_upper_list)
print(type(names_upper_list))