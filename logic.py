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


        self.submit_press_count = 0
        self.question_list = self.set_questions()

        #Home frame buttons
        self.to_quiz_button_home_frame.clicked.connect(lambda : self.home_frame.hide())
        
        #Quiz frame buttons
        self.quiz_submit_button.clicked.connect(lambda : self.submit_button())
        self.to_home_button_quiz_frame.clicked.connect(lambda : self.home_button_quiz_frame())

        #win/lose frame buttons
        self.to_quiz_button_win_lose_frame.clicked.connect(lambda : self.restart_button_win_lose_frame())
        self.to_home_button_win_lose_frame.clicked.connect(lambda : self.home_button_win_lose_frame())




    #Win/Lose frame buttons methods
    def home_button_win_lose_frame(self):
        self.win_lose_frame.hide()
        self.home_frame.show()
        self.restart_game()

    def restart_button_win_lose_frame(self):
        self.win_lose_frame.hide()
        self.restart_game()
        




    #Quiz frame button methods
    def change_to_win_lose_screen(self):
        self.win_lose_frame.show()

    def home_button_quiz_frame(self):
        self.restart_game()
        self.home_frame.show()




    def restart_game(self):
        '''
        resets all entries and sets labels back to default
        
        :return: None
        '''
        self.attempt_counter_label.setText("0/3 attempts")
        self.submit_press_count = 0
        self.win_lose_label.setText(" ")

        for question in self.question_list:
            question.get_text_entry_object().clear()
            question.get_text_entry_object().setStyleSheet("background-color: white;")





    def set_questions(self) -> None:
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
    



    def submit_button(self) -> None:
        '''
        Check if all answers are correct or if used all three attempts,, then change to win_lose_frame
        If all answers were correct, win_lose_frame will show that you won!
        If all answers were NOT correct, win_lose_frame will show that you lost

        
        :return: None
        '''

        #counting every submit button press
        self.submit_press_count += 1
        self.attempt_counter_label.setText(str(self.submit_press_count) + "/3 Attempts remaining")


        self.check_questions()
        #check questions method


        if self.check_quiz_status() == True:
            print("got all answers correct")
            self.change_to_win_lose_screen()
            self.win_lose_label.setText(f"CONGRATS YOU WON!! \nin {self.submit_press_count}/3 attempts")
            return

        if self.submit_press_count >= 3:
            print("out of attempts")
            self.change_to_win_lose_screen()
            self.win_lose_label.setText(f"out of attempts :(")
            return
        

        


        



    def check_questions(self) -> None:
        '''
        method checks user input,
        If user input matches text_entry_answer(from the question class object), then set isCorrect = True and change background green, else isCorrect = False background red
        *user input is applied with .lower().strip() methods

        :return: None
        '''
        for question in self.question_list:
            user_answer = question.get_text_entry_object().text()
            user_answer = user_answer.lower().strip()

            if user_answer != question.get_text_entry_answer():
                question.set_question_status(False)
                question.get_text_entry_object().setStyleSheet("background-color: rgb(150, 0, 0);")
                # print("no Match", question.get_hint_label_object())

            if user_answer == question.get_text_entry_answer():
                question.set_question_status(True)
                question.get_text_entry_object().setStyleSheet("background-color: rgb(0, 150, 0);")
                # print("MATCHHH", question.get_hint_label_object())




    def check_quiz_status(self) -> bool:
        '''
        method iterates through each question in questions_list

        :return: False if one question is incorrect, True if all questions are correct
        '''
        for question in self.question_list:
            if question.get_question_status() == False:
                return False
            
        #all of the questions are correct
        return True
    



 
