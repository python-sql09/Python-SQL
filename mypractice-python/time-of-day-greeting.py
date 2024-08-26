# 17.22 Time of day greeting
import datetime
noon = datetime.time(12,00,00)
current_time = datetime.datetime.now().time()
if current_time >= noon:
    print("Good afternoon!")
elif current_time < noon:
    print("Good morning!")
while True:
    user_input = input("Would you like to enter a time? [Type quit to exit] ")
    if user_input.lower() == 'quit':
        break
    elif user_input.lower() == 'yes':
        user_input_time = input("Enter a time [HH:MM:SS format]: ")
        time_split = [int(i) for i in user_input_time.split(":")]
        user_time = datetime.time(time_split[0],time_split[1],time_split[2])
        if user_time >= noon:
            print(str(user_time) + " is in the afternoon.")
        elif user_time < noon:
            print(str(user_time) + " is in the morning.")