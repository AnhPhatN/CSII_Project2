from PyQt6.QtWidgets import *
from gui import *
from question import *
# import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Superhero Quiz')

        self.win_lose_frame.hide()


        submit_press_count = 0

        # #From home frame to quiz
        self.to_quiz_button_home_frame.clicked.connect(lambda : self.home_frame.hide())
        self.to_home_button_quiz_frame.clicked.connect(lambda : self.home_frame.show())

        self.quiz_submit_button.clicked.connect(lambda : print("submit button pressed!"))

     #hiding frames to be displayed
        # self.voting_frame.hide()
        # self.total_votes_frame.hide()

        # #From the home frame, 
        # # #vote_for_button takes you to voting frame
        # # #total_votes_button takes you to total votes frame
        # self.vote_for_button.clicked.connect(lambda : self.display_voting_frame())
        # self.total_votes_button.clicked.connect(lambda : self.display_total_votes_frame())


        
    
        question_list = self.set_questions()


        print(question_list)


    



    def set_questions(self):
        '''
        creates questions as Question class, and changes the GUI to the question
        
        :return: None
        '''
        q1 = Question(self.q1_hint_label, "Bruce Wayne", self.q1_lineEdit, "batman")
        q2 = Question(self.q2_hint_label, "Clark Kent", self.q2_lineEdit, "superman")
        q3 = Question(self.q3_hint_label, "Bruce Banner", self.q3_lineEdit, "hulk")

        question_list = [q1, q2, q3]


        for question in question_list:
            question.get_hint_label_object().setText(question.get_hint_label_str())


        return question_list