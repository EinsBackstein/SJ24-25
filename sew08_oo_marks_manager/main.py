import controller
# Initial User Information
print("\n1 - Enter a Subject with mark \n2 - Remove a Subject \n3 - Show all subjects \n0 - Exit\n")

controller = controller.Controller()

def check_input(user_input):
    if (user_input == "0"):
        exit()
    elif (user_input == "1"):
        subject = input("Please input the subject: ")
        mark = int(input("Please input the mark: "))
        controller.save_subject(subject, mark)
    elif (user_input == "2"):
        subject = input("Please input the subject: ")
        controller.delete_subject(subject)
    elif (user_input == "3"):
        all = controller.all_subjects()
        for key,value in all.items():
            print(value)
    else:
        print("Invalid input, please try again.")
        user_input = input("Please input your choice: ")
        check_input(user_input)

user_input = input("Please input your choice: ")
while (True):
    try:
        check_input(user_input)
        user_input = input("Please input your choice again: ")
    except ValueError as e:
        print("Invalid input, please try again.")
    
