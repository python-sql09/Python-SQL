from flask import Flask, render_template, request
import random, string

app = Flask(__name__)

# Letter examples
letter_examples = {
    'A': ['Apple', 'Ant', 'Airplane', 'Alligator'],
    'B': ['Ball', 'Bear', 'Banana', 'Butterfly'],
    'C': ['Cat', 'Car', 'Cake', 'Cow'],
    'D': ['Dog', 'Duck', 'Dinosaur', 'Dolphin'],
    'E': ['Elephant', 'Egg', 'Eagle', 'Ear'],
    'F': ['Fish', 'Frog', 'Flower', 'Fire'],
    'G': ['Giraffe', 'Goat', 'Grape', 'Guitar'],
    'H': ['Horse', 'Hat', 'House', 'Heart'],
    'I': ['Ice cream', 'Igloo', 'Island', 'Insect'],
    'J': ['Jellyfish', 'Juice', 'Jacket', 'Jump'],
    'K': ['Kite', 'Kangaroo', 'Key', 'King'],
    'L': ['Lion', 'Lemon', 'Leaf', 'Lamp'],
    'M': ['Mouse', 'Moon', 'Monkey', 'Mountain'],
    'N': ['Nest', 'Net', 'Nose', 'Night'],
    'O': ['Ocean', 'Orange', 'Owl', 'Octopus'],
    'P': ['Pig', 'Pizza', 'Penguin', 'Plane'],
    'Q': ['Queen', 'Quail', 'Question', 'Quiet'],
    'R': ['Rabbit', 'Rain', 'Rainbow', 'Robot'],
    'S': ['Sun', 'Snake', 'Star', 'Smile'],
    'T': ['Tiger', 'Tree', 'Turtle', 'Train'],
    'U': ['Umbrella', 'Unicorn', 'Up', 'Under'],
    'V': ['Van', 'Violin', 'Volcano', 'Voice'],
    'W': ['Water', 'Whale', 'Window', 'Wind'],
    'X': ['Xylophone', 'X-ray', 'Xenon', 'Xerox'],
    'Y': ['Yellow', 'Yak', 'Yarn', 'Yawn'],
    'Z': ['Zebra', 'Zoo', 'Zipper', 'Zero']
}

@app.route('/')
def home():
    return render_template('index.html')

# Add all your other pages
@app.route('/learn-letters')
def learn_letters(): return render_template("learn-letters.html")

@app.route('/learn-numbers')
def learn_numbers(): return render_template("learn-numbers.html")

@app.route('/connect-letters')
def connect_letters(): return render_template("connect-letters.html")

@app.route('/connect-numbers')
def connect_numbers(): return render_template("connect-numbers.html")

@app.route('/learn-shapes')
def learn_shapes(): return render_template("learn-shapes.html")

@app.route('/count-items')
def count_items(): return render_template("count-items.html")

@app.route('/addition-game')
def addition_game(): return render_template("addition-game.html")

@app.route('/subtraction')
def subtraction(): return render_template("subtraction.html")

# 🎓 Kids Learn Letters route
@app.route('/kids-learn-letters')
def kids_learn_letters():
    mode = request.args.get("mode", "learn")
    alphabet = list(string.ascii_uppercase)

    if mode == "quiz":
        correct = request.args.get("correct")
        selected = request.args.get("letter")
        quiz_letter = random.choice(alphabet)
        quiz_example = random.choice(letter_examples[quiz_letter])
        options = list({quiz_letter, *random.sample(set(alphabet) - {quiz_letter}, 3)})
        random.shuffle(options)
        result = None
        if selected and correct:
            result = "correct" if selected == correct else "wrong"
        return render_template("kids-learn-letters.html", mode=mode, quiz_example=quiz_example,
                                options=options, correct=quiz_letter, result=result)

    current_letter = request.args.get("letter", "A")
    index = alphabet.index(current_letter)
    prev_letter = alphabet[index - 1] if index > 0 else 'Z'
    next_letter = alphabet[index + 1] if index < 25 else 'A'
    examples = ", ".join(letter_examples[current_letter])
    return render_template("kids-learn-letters.html", mode=mode, current_letter=current_letter,
                            examples=examples, prev_letter=prev_letter, next_letter=next_letter,
                            alphabet=alphabet)

if __name__ == "__main__":
    app.run(debug=True)