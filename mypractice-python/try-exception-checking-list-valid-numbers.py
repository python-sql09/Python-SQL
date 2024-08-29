# 22.8 Checking a list for valid values
def check_numbers(input_list):
    list = []
    for x in input_list:
        try:
            a = float(x)
            list.append(x)
        except ValueError:
            try:
                a = int(x)
                list.append(x)
            except (ValueError,ZeroDivisionError,TypeError):
                print(x + " is not a valid number.")
        except (ZeroDivisionError,TypeError) as e:
            print(x + " is not a valid number.")
    return list
input_list = [1,'c',"Haythem",23,6,6.7,-1,"String"]
print(input_list)
# check_numbers should return a list that contains the valid numbers.
numbers = check_numbers(input_list)
print(numbers)