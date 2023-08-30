from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

new_brain = QuizBrain(question_bank)

while new_brain.still_has_questions():
    new_brain.next_question()

if new_brain.score > 8:
    print("You are good!")
else:
    print("You suck!")
