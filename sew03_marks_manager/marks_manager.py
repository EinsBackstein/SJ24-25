# Initial User Information
print("\n1 - Enter a Subject with mark \n2 - Remove a Subject \n3 - Show all subjects \n0 - Exit\n")

grades = {}

class Subject:
    def __init__(self, name):
        self.name = name
        self.mark = {1,2,3}
    def add_mark(self, mark):
        self.mark.add(mark)
    def __str__(self):
        return f"Subject:\t {self.name} \nMark/s:\t\t {self.mark}\n"

user_input = input("Please input your choice: ")
def add_subject():
    input_subject = input("Please input the subject: ")
    input_mark = input("Please input the mark: ")

    if input_subject not in grades:
        subject = Subject(input_subject)
        grades[subject.name] = subject
        subject.add_mark(input_mark)
    else:
        grades[input_subject].add_mark(input_mark)

def remove_subject():
    print("Removing subject...")

def show_subjects():
    print("Showing subjects...")

def exit_program():
    print("Exiting program...")
    print("Goodbye!")
    exit()

def check_input(user_input):
    if(user_input == "0"):
        exit_program()
    elif(user_input == "1"):
        add_subject()
    elif(user_input == "2"):
        remove_subject()
    elif(user_input == "3"):
        show_subjects()
    else:
        print("Invalid input, please try again.")
        user_input = input("Please input your choice: ")
        check_input(user_input)

check_input(user_input)
