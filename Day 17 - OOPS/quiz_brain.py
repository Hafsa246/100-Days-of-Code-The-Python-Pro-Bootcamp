class QuizBrain:

    # Constructor - initializes attributes
    def __init__(self, ques_list):
        self.ques_num = 0
        self.ques_list = ques_list
        self.score = 0

    def sill_has_questions(self):
        # if self.ques_num == len(self.ques_list-1):
        #     return False
        # else:
        #     return True
        return self.ques_num < len(self.ques_list)

    def next_question(self):
        current_ques = self.ques_list[self.ques_num]
        self.ques_num += 1
        user_ans = input(f"Q.{self.ques_num}: {current_ques.text}. (True/False): ")
        self.check_answer(user_ans, current_ques.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.ques_num}")
        print("\n")
