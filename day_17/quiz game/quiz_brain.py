class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_qustion(self):
       return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans=input(f"Q. {self.question_number}:{current_question.text} (True/False) :")
        self.cheeck_ans(user_ans,current_question.answer)
    def cheeck_ans(self,user_ans,correct_answer):
        if user_ans.lower() == correct_answer.lower() :
            print("correct")
            self.score += 1
            print(f"your score is :{self.score}/{self.question_number}")
        else :
            print("false")
        print(f"The correct ans is :{correct_answer}")
        print("\n")

