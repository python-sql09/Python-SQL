# Exercise 4: Everywhere That Mary Went…
# The following code includes a set of the states that Mary has visited:
# Mary's visited states
mary_states = {"AZ", "CA", "FL", "GA", "IN", "KY", "MA", "NV", "NY", "NC", "PA", "SC", "TN", "WA", "WV", "WI", "WY", "OR"}

# All states
all_states = {"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", 
              "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", 
              "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"}

# Set to store the states the user has visited
user_states = set()

# Prompt the user to enter the state abbreviations they have visited
while True:
    state = input("Enter the abbreviation of a state you have visited (or 'done' to finish): ").upper()
    if state == "DONE":
        break
    elif state in all_states:
        user_states.add(state)
    else:
        print("Invalid state abbreviation. Please try again.")

# Combine both sets to see where either the user or Mary has visited
all_visited = user_states | mary_states

# Find out the states that neither Mary nor the user has visited
unvisited_states = all_states - all_visited

# Display the results
print("\nStates either you or Mary have visited:")
print(sorted(all_visited))

print("\nStates neither you nor Mary have visited:")
print(sorted(unvisited_states))