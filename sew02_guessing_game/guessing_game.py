from random import randint

max_number = input("Please put in the highest possible number to guess: ")

# only if first input is invalid
while max_number.isdigit() == False:
    max_number = input("Please put in the highest possible number to guess: ")

random_number = randint(1, int(max_number))

input_number = input("Please enter a number from 1 to " +
                     str(max_number) + " or 0 to exit : ")

# only if input is invalid
while input_number.isdigit() == False:
    input_number = input(
        "Not a number! Please enter a number from 1 to " + str(max_number) + " or 0 to exit : ")

inputs = []
inputs.append(int(input_number))

guessedOrExit = False

while (guessedOrExit == False):
    if int(input_number) == 0:
    #exit condition - 0
        print("Entered 0, bye!")
        guessedOrExit = True
    elif int(input_number) == int(random_number):
    #correct guess
        print("Congratulations, you guessed the number!")
        guessedOrExit = True
        print(inputs)
    else:
    #incorrect guess
        input_number = input(
            "Sorry, wrong number, try again! Please enter a number from 1 to " + str(max_number) + " or 0 to exit : ")
        #check if is valid input
        while input_number.isdigit() == False:
            input_number = input(
                "Not a number! Please enter a number from 1 to " + str(max_number) + " or 0 to exit : ")
        #check if num was already tried
        while (int(input_number) in inputs):
            input_number = input(
                "Number already used! Please enter a number from 1 to " + str(max_number) + " or 0 to exit : ")
            #check if is valid input
            while input_number.isdigit() == False:
                input_number = input(
                    "Not a number! Please enter a number from 1 to " + str(max_number) + " or 0 to exit : ")
        inputs.append(int(input_number))
