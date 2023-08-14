from data import Data
from score import Scoreboard
import random as rand
import html
from art import logo
#initiliaze the class generating question number and getting input from the score py file
class QuizBrain:
    def __init__(self,q_data):
        self.q_data=q_data
        self.q_number=0
        self.score=Scoreboard()
        self.q_text=""
        self.end_loop=True

#using html unscape to decode the encoded characters in the random question that gets generated. loads
#the function that will check the user answer and assign the user answer to a variable that gets compared throiugh the check_ans function to check if answer is correct
    def generate_question(self):
        if self.q_number<=len(self.q_data):
            self.q_number+=1
            new_q=rand.choice(self.q_data)
            self.q_text=html.unescape(new_q["question"])
            corr_ans=new_q["correct_answer"]
            user_ans=self.check_user_ans(self.q_text)
            self.check_ans(user_ans,corr_ans)
        else:
            self.end_loop=False
            print(logo)
            print(f"Final score {self.score.points}/{self.q_number}\nGAME OVER!!")

#check answer function will check the user answer if it matches the correct answer(both variables passed in from the previous function)
#finally if answer is correct it adds a point and prints out the appropriate statement. If its wrong it only prints to let the user know he got it wrong
    def check_ans(self,user_ans,crr_ans):
        try:
            if user_ans.title()== crr_ans.title():
                self.score.add_point()
                print(f"You got it right\nYour score is {self.score.points}/{self.q_number}")
            else:
                print(f"Sorry you got it wrong.\n"
                      f"Your score is {self.score.points}/{self.q_number}")
        except AttributeError:
            print(f"{user_ans} not available.\nPlease restart program!!")
            self.end_loop=False
            return None
#asks the question and checks the input if it is true or false
    def check_user_ans(self,q_text):
        try:
            user_ans=input(f"Q{self.q_number}: {q_text} (True/False)\n").title()
            if user_ans=="T" or user_ans=="Tr" or user_ans=="Truu" or user_ans=="True":
                return "True"
            elif user_ans=="F" or user_ans=="Fa" or user_ans=="Fal"or user_ans=="Fals" or user_ans=="False":
                return "False"
        except AttributeError:
                print(f"{user_ans} not available.\nQuestion is getting skipped")
                self.end_loop = False

