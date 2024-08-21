# 11.18 Deleting a set of account names
acct_names_1 = {"Hayden", "Rishi", "John"}
acct_names_2 = {"Hailee", "Kasen", "Dylan"}
acct_names_3 = {"Leah", "Maxwell", "Rory"}
print("acct_names_1", acct_names_1, "acct_names_2", acct_names_2, "acct_names_3",
acct_names_3)
user_input = input("Please enter a name: ").capitalize()
if user_input in acct_names_1:
    del acct_names_1
    print("Deleted acct_names_1")
elif user_input in acct_names_2:
    del acct_names_2
    print("Deleted acct_names_2")
elif user_input in acct_names_3:
    del acct_names_3
    print("Deleted acct_names_3")
else:
    print("The name you entered is not in any of the sets.")