import ex1, ex2, ex3, ex4

print("\n 1 - Is Prime \n 2 - Remove Vowels \n 3 - Count Tokens \n 4 - Trimm \n 0 - Exit\n")

def check_input(user_input):
        if (user_input == "0"):
            print("Exiting program...")
            print("Goodbye!")
            exit()
        elif (user_input == "1"):
            ex1.is_prime()
        elif (user_input == "2"):
            ex2.remove_vowels()
        elif (user_input == "3"):
            ex3.count_tokens()
        elif (user_input == "4"):
            ex4.trimm()
        else:
            print("Invalid input, please try again.")
            user_input = input("Please input your choice: ")
            check_input(user_input)


user_input = input("Please input your choice: ")
while True:
    check_input(user_input)
    user_input = input("Please input your choice again: ")