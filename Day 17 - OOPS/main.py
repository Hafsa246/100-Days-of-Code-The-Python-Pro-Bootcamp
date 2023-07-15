from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    ques_text = question["question"]
    ques_ans = question["correct_answer"]
    new_question = Question(ques_text, ques_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.sill_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.ques_num}")
