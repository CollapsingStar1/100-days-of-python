import question_model
import data
import quiz_brain

questionbank = []
def which_data():
    print(data.question_data)
data = data.question_data
def create_questions():
    for question in data:
        new_question = question_model.Question(question["text"], question["answer"])
        questionbank.append(new_question)

def print_question():
    for question in questionbank:
        print(question.question_text)
        print(question.answer)

create_questions()
quiz_brain = quiz_brain.QuizBrain(questionbank)

def quiz():
    while quiz_brain.still_has_questions():
        quiz_brain.next_question()


quiz()
