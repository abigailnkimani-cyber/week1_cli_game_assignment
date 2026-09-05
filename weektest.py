"""
Quiz Game - A command-line quiz application.

This script presents a randomized quiz to the user, tracks their score,
and provides feedback based on performance.
"""

# Import Python's built-in random module for shuffling questions and options.
import random

# ---------------------------------------------------------------------------
# Quiz Data
# ---------------------------------------------------------------------------
# A nested dictionary holding all questions. Each top-level key is a category
# name mapping to a list of "question dictionaries". Each question dictionary
# has:
#   - "question": the prompt string shown to the user
#   - "options":   a dict of choice-letter -> answer-text (A-D)
#   - "answer":    the letter whose value is the correct answer
quiz_data = {
    "math questions": [
        {
            "question": "What is 905 + 275?",
            "options": {"A": "1180", "B": "1181", "C": "1182", "D": "1183"},
            "answer": "A"
        },
        {
            "question": "What is 15 * 18?",
            "options": {"A": "256", "B": "126", "C": "270", "D": "206"},
            "answer": "C"
        },
        {
            "question": "What is the square of 66?",
            "options": {"A": "4356", "B": "4456", "C": "4556", "D": "4656"},
            "answer": "A"
        },
        {
            "question": "What is the cube of 5?",
            "options": {"A": "125", "B": "120", "C": "130", "D": "135"},
            "answer": "A"
        }
    ],
    "general knowledge questions": [
        {
            "question": "What is the capital of France?",
            "options": {"A": "London", "B": "Berlin", "C": "Paris", "D": "Madrid"},
            "answer": "C"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": {"A": "Earth", "B": "Jupiter", "C": "Saturn", "D": "Mars"},
            "answer": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": {"A": "Charles Dickens", "B": "William Shakespeare",
                        "C": "Mark Twain", "D": "Jane Austen"},
            "answer": "B"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": {"A": "O2", "B": "H2O", "C": "CO2", "D": "NaCl"},
            "answer": "B"
        }
    ],
    "history questions": [
        {
            "question": "Who was the first President of the United States?",
            "options": {"A": "Abraham Lincoln", "B": "George Washington",
                        "C": "Thomas Jefferson", "D": "John Adams"},
            "answer": "B"
        },
        {
            "question": "In which year did World War II end?",
            "options": {"A": "1945", "B": "1939", "C": "1918", "D": "1963"},
            "answer": "A"
        },
        {
            "question": "Who was the first man to step on the moon?",
            "options": {"A": "Buzz Aldrin", "B": "Yuri Gagarin",
                        "C": "Neil Armstrong", "D": "Michael Collins"},
            "answer": "C"
        },
        {
            "question": "What ancient civilization built the pyramids?",
            "options": {"A": "Romans", "B": "Greeks", "C": "Egyptians", "D": "Mayans"},
            "answer": "C"
        }
    ]
}

# ---------------------------------------------------------------------------
# Game Initialization
# ---------------------------------------------------------------------------
# Greet the player.
print("Welcome to the Quiz Game!")
print("You will be asked several questions. Try to answer them correctly.")

# Track correct answers and total questions attempted.
score = 0
total = 0

# ---------------------------------------------------------------------------
# Category Iteration (randomized)
# ---------------------------------------------------------------------------
# Convert the dict into a list of (key, value) pairs so it can be shuffled.
categories = list(quiz_data.items())
random.shuffle(categories)  # randomize the order categories appear in

# Iterate one category at a time.
for category, questions in categories:
    print(f"\nCategory: {category}")  # announce which category is up
    random.shuffle(questions)         # randomize question order within category

    # Present up to 5 questions (each category only has 4, so all are used).
    for i, question_data in enumerate(questions[:5], start=1):
        print(f"\nQuestion {i}: {question_data['question']}")

        # --- Shuffle the answer options (A/B/C/D) ---
        # Grab the original (letter, text) pairs as a list.
        option_items = list(question_data["options"].items())
        random.shuffle(option_items)  # randomize their display order

        # Reassign letters A, B, C, D based on the shuffled order, and
        # remember which new letter holds the originally-correct answer.
        shuffled_options = {}
        correct_letter = None
        for idx, (orig_key, value) in enumerate(option_items):
            new_key = ["A", "B", "C", "D"][idx]      # assign a fresh letter
            shuffled_options[new_key] = value
            if orig_key == question_data["answer"]:  # was this the correct one?
                correct_letter = new_key

        # Display each option on its own line.
        for option_key, option_value in shuffled_options.items():
            print(f"{option_key}. {option_value}")

        # --- Get the user's answer ---
        # Keep prompting until the user enters a valid letter A-D.
        # An inner try/except catches EOFError (closed pipe) and non-A-D
        # input, printing an error and re-prompting instead of crashing.
        while True:
            try:
                # .strip() removes leading/trailing whitespace so '  a  '
                # is accepted; .upper() normalizes the case to 'A'.
                user_answer = input("Enter your answer (A, B, C, D): ").strip().upper()
            except EOFError:
                # Input stream closed (e.g. empty pipe) — retry the prompt.
                print("\nInput error. Please try again.")
                continue

            # Reject anything that isn't one of the four valid letters.
            if user_answer not in ("A", "B", "C", "D"):
                print("Invalid choice. Please enter A, B, C, or D.")
                continue

            break  # valid answer obtained — exit the validation loop

        # --- Evaluate the answer ---
        if user_answer == correct_letter:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_letter}.")

        total += 1
        percentage_score = (score / total) * 100 if total else 0
        print(f"\nYour score: {score}/{total} ({percentage_score:.2f}%)")

        # Performance feedback that updates as the quiz progresses.
        if percentage_score >= 80:
            print("Awesome! You have a great understanding of the material.")
        elif percentage_score >= 50:
            print("Good job! Keep practicing to improve.")
        else:
            print("Keep trying! You're almost there.")
