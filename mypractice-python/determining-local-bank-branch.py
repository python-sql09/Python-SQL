# 11.22 Determining a local bank branch
branch_states = {"AZ", "CA", "FL", "GA", "IN", "KY", "MA", "NV", "NY", "NC",
"PA", "SC", "TN"}
local_states = set()
user_input = input("Please enter the abbreviation of a state that is local to you \
[type 'done' to quit]: ").upper()
while user_input != 'DONE':
    local_states.update({user_input})
    user_input = input("Please enter another abbreviation of a state that is local \
to you [type 'done' to quit]: ").upper()
local_branches = branch_states.intersection(local_states)
if not local_branches:
    print("You are not local to any bank branches.")
else:
    print(branch_states.intersection(local_states))