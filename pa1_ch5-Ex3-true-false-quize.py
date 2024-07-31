# Exercise 3: True or False Quiz
# List of questions and their correct answers
questions = [
    {"question": "The Earth is flat.", "answer": False},
    {"question": "Python is a programming language.", "answer": True},
    {"question": "The Sun rises in the west.", "answer": False},
    {"question": "Water boils at 100 degrees Celsius.", "answer": True},
    {"question": "Humans can breathe underwater without any equipment.", "answer": False}
]
user_answers = []
# Ask the user each question
for i, q in enumerate(questions, start=1):
    user_answer = input(f"Question {i}: {q['question']} (True/False): ").strip().lower()
    if user_answer == "true":
        user_answers.append(True)
    elif user_answer == "false":
        user_answers.append(False)
    else:
        print("Invalid input. Please answer with True or False.")
# Calculate the number of correct answers
correct_count = sum(1 for i, q in enumerate(questions) if q['answer'] == user_answers[i])
# Display the questions, correct answers, and user's answers
print("\nQuiz Results:")
for i, q in enumerate(questions, start=1):
    correct_answer = "True" if q['answer'] else "False"
    user_answer = "True" if user_answers[i-1] else "False"
    print(f"Question {i}: {q['question']}")
    print(f"Correct answer: {correct_answer}")
    print(f"Your answer: {user_answer}\n")
# Calculate and display the user's correct response rate
response_rate = correct_count / len(questions)
print(f"Your correct response rate: {response_rate:.2%}")
