# Initial User Information
print("\n1 - Enter a Subject with mark \n2 - Remove a Subject \n3 - Show all subjects \n0 - Exit\n")

class Subject:
    def __init__(self, name):
        self.name = name
        self.mark = []

    def add_mark(self, mark):
        self.mark.append(mark)

    def __str__(self):
        return f"\nSubject:\t {self.name} \nMark/s:\t\t {self.mark}"

class Grades:
    def __init__(self):
        self.grades = {}

    def add_subject(self):
        input_subject = input("Please input the subject: ")
        input_mark = input("Please input the mark: ")

        if input_subject not in self.grades:
            print("Adding new subject...")
            subject = Subject(input_subject)
            subject.add_mark(int(input_mark))
            self.grades[subject.name] = subject
        else:
            print("Subject already exists, adding mark...")
            self.grades[input_subject].add_mark(int(input_mark))

        print(self.grades[input_subject])

    def remove_subject(self):
        input_subject = input("Please input the subject: ")
        if input_subject in self.grades:
            print("Removing subject...")
            del self.grades[input_subject]
        else:
            print("Subject does not exist, try looking up subjects.")

    def show_subjects(self):
        for value in self.grades.values():
            print(value)

    def exit_program(self):
        print("Exiting program...")
        print("Goodbye!")
        exit()

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

# def remove_subject():
#     input_subject = input("Please input the subject: ")
#     if input_subject in grades:
#         print("Removing subject...")
#         del grades[input_subject]
#     else:
#         print("Subject does not exist, try looking up subjects.")


# def show_subjects():
#     for value in grades.values():
#         print(value)


# def exit_program():
#     print("Exiting program...")
#     print("Goodbye!")
#     exit()


# def check_input(user_input):
#     if (user_input == "0"):
#         grades.exit_program()
#     elif (user_input == "1"):
#         grades.add_subject()
#     elif (user_input == "2"):
#         grades.remove_subject()
#     elif (user_input == "3"):
#         grades.show_subjects()
#     else:
#         print("Invalid input, please try again.")
#         user_input = input("Please input your choice: ")
#         check_input(user_input)


while (True):
    grade.check_input(user_input)
    user_input = input("Please input your choice again: ")
