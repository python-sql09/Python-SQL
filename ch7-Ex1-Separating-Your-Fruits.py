# Exercise 1: Separating Your Fruits
# Given the list fruit_list, write a script that iterates through the list and prints 
# each item on a separate line:
fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]
# your code here
for fruit in fruit_list:
    print(fruit)
    for letter in fruit:
        print(letter.upper())
    print("- - - - - -")

fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]
for fruit in fruit_list:
    print(fruit)