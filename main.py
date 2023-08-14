from data import Data
from quiz_brain import QuizBrain
from score import Scoreboard
from art import logo
#prints logo
print(logo)

#initialize classes and generate options list
data=Data()
options=data.generate_options_list()

#get user input to decide category
cat=input(f"What category would you like to choose?\n"
          f"{options}\n").title()
#generates the list of dictionaries that contain questions and answers
q_data=data.choose_url(cat)
brain=QuizBrain(q_data)
score=Scoreboard()

try:
    while brain.end_loop:
        brain.generate_question()

#in case the input does not exist it terminates the program and asks user to restart
except TypeError:
    print("Program not working.\nPlease restart")
