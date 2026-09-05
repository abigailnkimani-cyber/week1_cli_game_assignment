# Quiz Game - Code Manual

A command-line quiz application written in Python. It presents a randomized set
of questions, collects answers, tracks the score, and gives feedback.

---

## 1. File Overview

| File          | Purpose                                                       |
|---------------|---------------------------------------------------------------|
| `weektest.py` | The main game script (logic + data).                          |
| `README.md`   | This manual.                                                  |

---

## 2. Running the Game

```bash
python weektest.py
```

**Requirements:** Python 3.x (uses only the standard library — no pip installs).

You will be prompted to enter `A`, `B`, `C`, or `D` for each question.

---

## 3. High-Level Execution Flow

```
[Start]
   |
   v
Print welcome message
   |
   v
Shuffle category order
   |
   v
For each category (shuffled):
       Shuffle questions within the category
       For each question (up to 5):
            Shuffle answer options (A-D)
            Print the question and options
            Prompt the user for input
            Validate / grade the answer
            Update score and show feedback
   |
   v
End (score is shown after every question)
```

---

## 4. Data Structure (`quiz_data`)

All questions are stored in a single nested dictionary called `quiz_data`:

```
quiz_data
├── "math questions"                 -> list of question dicts
├── "general knowledge questions"    -> list of question dicts
└── "history questions"              -> list of question dicts
```

Each **question dict** has three keys:

| Key        | Type     | Description                                              |
|------------|----------|----------------------------------------------------------|
| `question` | `str`    | The prompt shown to the player.                          |
| `options`  | `dict`   | Maps letter keys `"A".."D"` to option text.              |
| `answer`   | `str`    | The letter (`"A"`/`"B"`/`"C"`/`"D"`) of the correct option. |

---

## 5. Section-by-Section Walkthrough

### 5.1 Import
```python
import random
```
Brings in Python's `random` module, used for all shuffling.

### 5.2 Data
```python
quiz_data = { ... }
```
Holds every question, grouped by category (see Section 4).

### 5.3 Initialization
```python
print("Welcome to the Quiz Game!")
print("You will be asked several questions. Try to answer them correctly.")
score = 0
total = 0
```
- Prints a greeting.
- `score` — counts correct answers.
- `total` — counts questions attempted.

### 5.4 Randomize category order
```python
categories = list(quiz_data.items())
random.shuffle(categories)
```
Dictionaries preserve insertion order in Python 3.7+, but to vary each run
we convert items to a list and shuffle it. Now the first category shown is
random (math / general / history).

### 5.5 The main category loop
```python
for category, questions in categories:
    print(f"\nCategory: {category}")
    random.shuffle(questions)
    for i, question_data in enumerate(questions[:5], start=1):
        ...
```
- `enumerate(questions[:5], start=1)` takes up to 5 questions from the
  (shuffled) list, numbering them 1..5.
- Each category has 4 questions, so all four display.

### 5.6 Randomizing the answer options
```python
option_items = list(question_data["options"].items())
random.shuffle(option_items)

shuffled_options = {}
correct_letter = None
for idx, (orig_key, value) in enumerate(option_items):
    new_key = ["A", "B", "C", "D"][idx]
    shuffled_options[new_key] = value
    if orig_key == question_data["answer"]:
        correct_letter = new_key
```
Why this is needed: the `options` dict stores answers by original letter
(`A`, `B`, `C`, `D`), and `answer` refers to one of those original letters.
After shuffling the dict items we cannot keep the old keys. This block:

1. Converts `(letter, text)` pairs to a list and shuffles it.
2. Reassigns the letters `A`, `B`, `C`, `D` based on position 0-3 of the
   shuffled list.
3. Finds which new letter now corresponds to the originally-correct answer
   and saves it in `correct_letter`.

### 5.7 Display options
```python
for option_key, option_value in shuffled_options.items():
    print(f"{option_key}. {option_value}")
```
Prints each randomized option on its own line.

### 5.8 Getting input
```python
try:
    user_answer = input("Enter your answer (A, B, C, D): ").upper()
except EOFError:
    print("\nInput error. Please try again.")
    continue
```
- Reads a line and upper-cases it so `c` and `C` both work.
- `EOFError` covers cases where input is unavailable (e.g., piped with no
  data when the stream closes).

### 5.9 Grading
```python
if user_answer == correct_letter:
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The correct answer is {correct_letter}.")
```
Compares the user's letter to `correct_letter` (the freshly mapped correct
letter, not the original one).

### 5.10 Score & feedback
```python
total += 1
percentage_score = (score / total) * 100 if total else 0
print(f"\nYour score: {score}/{total} ({percentage_score:.2f}%)")
if percentage_score >= 80:
    print("Awesome! ...")
elif percentage_score >= 50:
    print("Good job! ...")
else:
    print("Keep trying! ...")
```
- Increments `total` for every attempt.
- Computes a running percentage.
- Gives tiered feedback:
  - **>= 80 %** — "Awesome!"
  - **50–79 %** — "Good job!"
  - **< 50 %** — "Keep trying!"

---

## 6. Key Concepts Recap

| Concept              | Where it happens                          |
|----------------------|-------------------------------------------|
| Random category order| `random.shuffle(categories)`              |
| Random question order| `random.shuffle(questions)` per category  |
| Random option layout | `random.shuffle(option_items)` per question|
| Answer remapping     | `correct_letter` tracking loop            |
| Running score        | `score` and `total` variables             |
| Grade thresholds     | `if/elif/else` on `percentage_score`      |

---

## 7. Customization Tips

- **Add more questions:** append dicts to the relevant list inside
  `quiz_data`, following the same `question`/`options`/`answer` shape.
- **Change how many questions are asked:** edit `questions[:5]` — e.g.
  `[:10]` for up to 10 per category.
- **Add categories:** add a new top-level key to `quiz_data`; it's picked up
  automatically.
- **Adjust difficulty feedback:** modify the numeric thresholds
  (`80`, `50`) or the message strings.
