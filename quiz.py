import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        question_types = (Add, Multiply)
        # generate 10 random quesitons with numbers from 1 - 10
        for _ in range(10):
            # extensivle opptortunity
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)
            # add these questions to self.questions
            self.questions.append(question)

    def take_quiz(self):
        # log the start time
        # ask all the questions
        # log if they got the question right
        # log the end time
        # show a summary
        pass

    def ask(self, question):
        # log the start time
        # capture the answer
        # check the answer
        # log the end time
        # if the answer is right, send back True
        # otherwise send back False
        # send back the elapsed time, too
        pass

    def total_correct(self):
        # return the total number correct
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        # print how many you got right & total # of questions: 5/10
        print("You got {} out of {} right!".format(self.total_correct(), len(
            self.questions)))
        # print the total time for the quiz: 30 seconds
        print("It took you {} seconds total.".format((
            self.end_time - self.start_time).seconds))
