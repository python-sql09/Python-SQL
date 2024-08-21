# Checking a credit score
creditscore = int(input("Please enter a credit score: "))
if creditscore <= 450:
    print("This credit score is very low.")
elif creditscore <= 650 and creditscore > 450:
    print("This credit score is low.")
elif creditscore <= 800 and creditscore > 650:
    print("This credit score is good.")
elif creditscore > 800 and creditscore <= 850:
    print("This credit score is excellent.")
else:
    print("Please enter a valid credit score between 0 and 850")
