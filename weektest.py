import random
#questions to be asked
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
        "options": {"A": "Charles Dickens", "B": "William Shakespeare", "C": "Mark Twain", "D": "Jane Austen"},
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": {"A": "O2", "B": "H2O", "C": "CO2", "D": "NaCl"},
        "answer": "B"
    }

],
"history questions":[
    {
        "question": "Who was the first President of the United States?",
        "options": {"A": "Abraham Lincoln", "B": "George Washington", "C": "Thomas Jefferson", "D": "John Adams"},
        "answer": "B"
    },
    {
        "question": "In which year did World War II end?",
        "options": {"A": "1945", "B": "1939", "C": "1918", "D": "1963"},
        "answer": "A"
    },
    {
        "question": "Who was the first man to step on the moon?",
        "options": {"A": "Buzz Aldrin", "B": "Yuri Gagarin", "C": "Neil Armstrong", "D": "Michael Collins"},
        "answer": "C"
    },
    {
        "question": "What ancient civilization built the pyramids?",
        "options": {"A": "Romans", "B": "Greeks", "C": "Egyptians", "D": "Mayans"},
        "answer": "C"
    }
]
}
 #quiz_data = quiz_data["math questions"] + quiz_data["general knowledge questions"] + quiz_data["history questions"]  
print("Welcome to the Quiz Game!") 
print("You will be asked several questions. Try to answer them correctly.")

score = 0
total = 0

for category, questions in quiz_data.items():
    print(f"\nCategory: {category}")
    random.shuffle(questions)
    for i, question_data in enumerate(questions[:5], start=1):
        print(f"\nQuestion {i}: {question_data['question']}")
        for option_key, option_value in question_data["options"].items():
            print(f"{option_key}. {option_value}")
    try:
        user_answer = input("Enter your answer (A, B, C, D): ").upper()
    except EOFError:print("\nInput error. Please try again.")

    user_answer = input("Enter your answer (A, B, C, D): ").upper()
    if user_answer == question_data["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question_data['answer']}.")
    total += 1
    #final score
    percentage_score = (score/total) * 100 if total else 0
    print(f"\nYour score: {score}/{total} ({percentage_score:.2f}%)")
    if percentage_score >= 80:
        print("Awesome! You have a great understanding of the material.")
    elif percentage_score >= 50:
        print("Good job! Keep practicing to improve.")
    else:
        print("Keep trying! You're almost there.")





