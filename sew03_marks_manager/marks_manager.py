# Initial User Information
print("\n1 - Enter a Subject with mark \n2 - Remove a Subject \n3 - Show all subjects \n0 - Exit\n")

# Class Definitions

# Class Subject - add and show marks
class Subject:
    def __init__(self, name):
        self.name = name
        self.mark = []

    def add_mark(self, mark):
        self.mark.append(mark)

    def __str__(self):
        return f"\nSubject:\t {self.name} \nMark/s:\t\t {self.mark}"

# Class Grades - add, remove and show subjects | exit program | exeption handling
class Grades:
    def __init__(self):
        self.grades = {}
    # adds subject and mark to grades dict
    def add_subject(self):
        input_subject = input("Please input the subject: ")
        input_mark = input("Please input the mark: ")
        # Check if subject exists | add new subject | add mark to existing subject
        if input_subject not in self.grades:
            print("Adding new subject...")
            subject = Subject(input_subject)
            subject.add_mark(int(input_mark))
            self.grades[subject.name] = subject
        else:
            print("Subject already exists, adding mark...")
            self.grades[input_subject].add_mark(int(input_mark))

        print(self.grades[input_subject])
    # removes subject and its marks from grades dict
    def remove_subject(self):
        input_subject = input("Please input the subject: ")
        if input_subject in self.grades:
            print("Removing subject...")
            del self.grades[input_subject]
        else:
            print("Subject does not exist, try looking up subjects.")
    # shows all subjects and their marks
    def show_subjects(self):
        for value in self.grades.values():
            print(value)
    # exits program
    def exit_program(self):
        print("Exiting program...")
        print("Goodbye!")
        exit()
    # checks user input | exception handling
    def check_input(self,user_input):
        if (user_input == "0"):
            self.exit_program()
        elif (user_input == "1"):
            self.add_subject()
        elif (user_input == "2"):
            self.remove_subject()
        elif (user_input == "3"):
            self.show_subjects()
        else:
            print("Invalid input, please try again.")
            user_input = input("Please input your choice: ")
            self.check_input(user_input)

grade = Grades()
user_input = input("Please input your choice: ")

while (True):
    grade.check_input(user_input)
    user_input = input("Please input your choice again: ")
