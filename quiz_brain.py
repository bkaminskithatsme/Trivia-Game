class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        ans = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?")
        if ans.lower() == self.question_list[self.question_number].answer.lower():
            print("Thats Right!")
            self.score += 1
            print(f"Your Score is {self.score}/{self.question_number +1} \n")
        else:
            print("Wrong wrong...")
            print(f"Your Score is {self.score}/{self.question_number + 1} \n")
        self.question_number += 1

    def still_has_questions(self):
        if len(self.question_list) == self.question_number:
            return False
        else:
            return True
