# 11.20 States where the user doesn’t have access
states_abbrev = {"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI",
"ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
"MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR",
"PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"}
user_input = input("Please enter the abbreviation of a state that is local to you [type 'done' to quit]: ").upper()
local_states = set()
while user_input != 'DONE':
    local_states.update({user_input})
    user_input = input("Please enter another abbreviation of a state near you [type /'done' to quit]: ").upper()
print(states_abbrev.difference(local_states))