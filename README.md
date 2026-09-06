# Quiz Game - Code Manual

A command-line quiz application written in Python. It presents a randomized set
of questions, collects answers, tracks the score, and gives feedback.

## Features
* Multiple-choice questions (A, B, C, D) across 3 categories
* Choose how many questions you want to answer (up to 12)
* Questions are shuffled into a random order each time you play
* Invalid input (anything other than A, B, C, or D) is caught and re-prompted
* Final score shown as a fraction and percentage, with a performance message

## Requirements
Python 3, import random from the standard in built library

No external libraries needed — only the built-in random module.

## How to Run
'''bash
python weektest_fixed.py
'''
## How to Play
When prompted, enter how many questions you'd like to answer.
For each question, type the letter (A, B, C, or D) matching your answer and press Enter.
After the last question, your score and percentage will be displayed, along with a short verdict:
80%+ → Excellent
50–79% → Good
Below 50% → Try again
## License
MIT
 
