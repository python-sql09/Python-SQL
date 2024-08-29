# 21.11 Using lambdas and map together
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)
print(list_numbers)
print(tuple_numbers)
map_iterator = map(lambda x, y: x + y, list_numbers, tuple_numbers)
map_list= list(map_iterator) # convert map output to a list
print(map_list)