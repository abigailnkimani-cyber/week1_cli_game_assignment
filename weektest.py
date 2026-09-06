import random

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


# Game Initialization

# Greet the player.
print("Welcome to the Quiz Game!")
print("You will be asked several questions. Try to answer them correctly.")

# Track correct answers and total questions attempted.
score = 0
total = 0

all_questions = []
for category, questions in quiz_data.items():
    for q in questions:
        q["category"] = category  # tag each question with its category
        all_questions.append(q)
 
random.shuffle(all_questions)
 
# Ask how many questions the player wants, with input validation.
max_questions = len(all_questions)
try:
    num_questions = int(input(f"How many questions do you want? (1-{max_questions}): "))
    if num_questions <= 0:
        print("Please enter a positive number.")
        num_questions = max_questions
    elif num_questions > max_questions:
        print(f"You can only answer up to {max_questions} questions. Setting to {max_questions}.")
        num_questions = max_questions
except ValueError:
    print("That's not a valid number.")
    num_questions = max_questions
 
questions_to_ask = all_questions[:num_questions]
 
current_category = None
for question in questions_to_ask:
    # Prints a category header whenever the category changes
    if question["category"] != current_category:
        current_category = question["category"]
        print(f"\n--- {current_category.title()} ---")
 
    print(f"\n{question['question']}")
    for option, text in question["options"].items():
        print(f"{option}. {text}")
 
    # Validate input: keep asking until it's a real option
    while True:
        user_answer = input("Enter your answer (A, B, C, D): ").upper()
        if user_answer in question["options"]:
            break
        print("Invalid choice — please enter A, B, C, or D.")
 
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question['answer']}.")
    total += 1
 
# Final score — printed once, after every question has been asked
percentage_score = (score / total) * 100 if total else 0
print(f"\nYour score: {score}/{total} ({percentage_score:.2f}%)")
if percentage_score >= 80:
    print("Excellent")
elif percentage_score >= 50:
    print("Good")
else:
    print("Try again")
