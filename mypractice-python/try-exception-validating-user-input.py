# 22.6 Validating user input
value_1 = input("Please enter a number: ")
value_2 = input("Please enter a second number [do not enter 0]: ")
try:
    x = int(value_1)/int(value_2)
    print(x)
except ValueError:
    try:
        x = float(value_1)/float(value_2)
        print(x)
    except ValueError:
        try:
            x = float(value_1)
        except:
            print("The first value entered is not an integer or a float.")
        try:
            x = float(value_2)
        except:
            print("The second value entered is not an integer or a float.")
except ZeroDivisionError:
    print("Oops, there's a zero in the second value. You can't divide by zero.")
    