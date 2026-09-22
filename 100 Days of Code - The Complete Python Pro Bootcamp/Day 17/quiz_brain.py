class QuizBrain:
    score = 0
    def __init__(self, question_list, question_number=0):
        self.question_list = question_list
        self.question_number = question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.question_text} (True/False):").lower().strip()
        self.check_answer(user_input, current_question.answer)
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower().strip() == correct_answer.lower().strip():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was {correct_answer}")
        self.score_board()
        print("\n")

    def score_board(self):
        print(f"You got {self.score} out of {len(self.question_list)} questions correct.")