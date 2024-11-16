from subject import Subject

class Controller:
    def __init__(self):
        self._grades:dict[str, object] = {}

    def save_subject(self, subject:str, mark:int):
        if(subject in self._grades):
            self._grades[subject].mark = mark
        else: 
            self._grades[subject] = Subject(subject, mark)

    def delete_subject(self, subject:str):
        if(subject in self._grades):
            del self._grades[subject]
        else:
            raise ValueError("Subject does not exist")
    def get_subject(self, title:str):
        return self._grades[title]
    def all_subjects(self):
        return self._grades

    