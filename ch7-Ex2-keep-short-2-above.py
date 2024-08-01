# Exercise 2: Keeping It Short
# Create a program that takes an input list of strings, identifies all the strings with two or
# more characters, and stores the results in another list. For example, the following list
# a = ["a", "bc", "rye", "hello", "c", ""]
# would produce the following output:
# ["bc", "rye", "hello"]
a = ["a", "bc", "rye", "hello", "c", ""]
print(a)
a.sort()
print(a)
# Create a new list to store strings with two or more characters
result = [item for item in a if len(item) >= 2]
