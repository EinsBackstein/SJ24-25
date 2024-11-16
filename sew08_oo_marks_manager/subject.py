class Subject:
    def __init__(self, subject:str, mark:int):
        self._subject = subject
        self._mark = []
        self.mark = mark 
    @property
    def mark(self):
        return self._mark
    @property
    def subject(self):
        return self._subject
    
    @mark.setter
    def mark(self, value:int):
        if(type(value) != int):
            raise ValueError("Mark must be an integer")
        elif(value < 1 or value > 5):
            raise ValueError("Mark must be between 1 and 5")
        else:
              self._mark.append(value)
    @subject.setter
    def subject(self, value:str):
        if(type(value) != str or value.__len__ <= 0):
            raise ValueError("Subject must be a string")
        else:
            self._subject = value

    def __str__(self):
        return f"\nSubject:\t {self.subject} \nMark/s:\t\t {self.mark}"

    def __eq__(self, other):
        if isinstance(other, Subject):
            return self._mark == other._mark and self.subject == other.subject 
        else: 
            return False

