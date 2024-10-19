import ex3
import ex4
import ex5

print("\n 1 - read/load file \n 2 - print data \n 3 - write/dump file \n 0 - Exit\n")


def check_input(user_input):
    if (user_input == "0"):
        print("Exiting program...")
        print("Goodbye!")
        exit()
    elif (user_input == "1"):
        read_file = input("Please input a file path: ")
        if (read_file.endswith(".csv")):
            print(ex4.read_colors("./home/"+read_file))
        else:
            print(ex5.load_colors("./home/", read_file))
    elif (user_input == "2"):
        print_data = input("Please input a file path: ")
        print_data = ex4.read_colors("./home/"+print_data)
        ex4.print_colors(print_data)
    elif (user_input == "3"):
        write_file = input("Please input a file path: ")
        data = [
            {"name": "Joe", "favorite_color": "blue"},
            {"name": "Anne", "favorite_color": "green"},
            {"name": "Bailey", "favorite_color": "red"},
        ]
        if (write_file.endswith(".csv")):
            ex3.write_colors("./home/", write_file, data)
        else:
            ex5.dump_colors("./home/", write_file, data)
    else:
        print("Invalid input, please try again.")
        user_input = input("Please input your choice: ")
        check_input(user_input)


check_input(input("Please input your choice: "))
