from urllib.request import urlopen
import json
import random as rand

#dictionary file with category name as key and url links as value
URL_DICT = {"General Knowledge":
                    "https://opentdb.com/api.php?amount=50&category=9&type=boolean",
                "Entertainment: Books":
                    "https://opentdb.com/api.php?amount=50&category=10&type=boolean",
                "Entertainment: Films":
                    "https://opentdb.com/api.php?amount=50&category=11&type=boolean",
                "Entertainment: Music":
                    "https://opentdb.com/api.php?amount=50&category=12&type=boolean",
                "Entertainment: Television":
                    "https://opentdb.com/api.php?amount=50&category=14&type=boolean",
                "Entertainment: Video Games":
                    "https://opentdb.com/api.php?amount=50&category=15&type=boolean",
                "Science & Nature":
                    "https://opentdb.com/api.php?amount=50&category=17&type=boolean",
                "Science: Computers":
                    "https://opentdb.com/api.php?amount=50&category=18&type=boolean",
                "Science: Mathematics":
                    "https://opentdb.com/api.php?amount=50&category=19&type=boolean",
                "Mythology":
                    "https://opentdb.com/api.php?amount=50&category=20&type=boolean",
                "Sports":
                    "https://opentdb.com/api.php?amount=50&category=21&type=boolean",
                "Geography":
                    "https://opentdb.com/api.php?amount=50&category=22&type=boolean",
                "History":
                    "https://opentdb.com/api.php?amount=50&category=23&type=boolean",
                "Politics":
                    "https://opentdb.com/api.php?amount=50&category=24&type=boolean",
                "Art":
                    "https://opentdb.com/api.php?amount=50&category=25&type=boolean",
                "Celebrities":
                    "https://opentdb.com/api.php?amount=50&category=26&type=boolean",
                "Entertainment: Comics":
                    "https://opentdb.com/api.php?amount=50&category=29&type=boolean"}

class Data:

#initialize this class and run the generate options list as soon as the file is opened
    def __init__(self):
        self.q_data=[]
        self.url=""
        self.generate_options_list()
        self.end_loop=True

#returns option list as one massive string
    def generate_options_list(self):
        options=""
        for opt in URL_DICT.keys():
            options+=f"{opt}/ "
        return options

#reads the category input in a request to open the url and download the json file. key error exception to catch any mistakes that the user might make
    def choose_url(self,cat):
        try:
            response=urlopen(URL_DICT[cat])
            data=json.loads(response.read())["results"]
        except KeyError:
            print("Category not found. \nRestart program")
            return None
        except UnboundLocalError:
            data={}
#loops through the list of questions and generates a new list in a random order . each time a question is loaded that question is removed
#from the questions list and added to a new one so the order is always random. Finally it returns the new list
        while data:
            new_q=rand.choice(data)
            data.remove(new_q)
            self.q_data.append(new_q)
        return self.q_data
