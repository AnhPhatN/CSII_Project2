



class Question:
    def __init__(self, hint_label_object, hint_label_str: str, text_entry_object, text_entry_answer: str):
        self.__hint_label_object = hint_label_object
        self.__hint_label_str = hint_label_str
        self.__text_entry_object = text_entry_object
        self.__text_entry_answer = text_entry_answer

        self.__isCorrect = False


    def __str__(self):
        return f'hint object: {self.__hint_label_object}, hint str: {self.__hint_label_str}, text object: {self.__text_entry_object}, text ans: {self.__text_entry_answer}, isCorrect: {self.__isCorrect}'
    
    

    def get_hint_label_object(self):
        return self.__hint_label_object
    
    def get_hint_label_str(self):
        return self.__hint_label_str

    def get_text_entry_object(self):
        return self.__text_entry_object
    
    def get_text_entry_answer(self):
        return self.__text_entry_answer
    

    def get_question_status(self):
        return self.__isCorrect

    


    