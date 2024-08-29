# Exercise 15: Self-Assessment
from datetime import datetime
import random
# Function to extract and return the date from a datetime object
def dateReturn(dt):
    return (lambda x: x.date())(dt)
# Function to extract and return the time from a datetime object
def timeReturn(dt):
    return (lambda x: x.time())(dt)
# Function to extract and return the first word from a string
def oneWord(text):
    return (lambda x: x.split()[0])(text)
# Optional: Function to return a random word from a string
def randomWord(text):
    words = text.split()
    return random.choice(words)
# Main script with user prompts
def main():
    # User input for datetime
    datetime_str = input("Enter a datetime (YYYY-MM-DD HH:MM:SS): ")
    dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    # User input for string
    text = input("Enter a string with multiple words: ")
    # Print results
    print(f"Date: {dateReturn(dt)}")
    print(f"Time: {timeReturn(dt)}")
    print(f"First word: {oneWord(text)}")
    print(f"Random word: {randomWord(text)}")

if __name__ == "__main__":
    main()