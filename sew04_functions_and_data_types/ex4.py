def trimm(s:str) -> str:
    s = s.replace(" ", "")
    return s

if(__name__ == "__main__"):
    trim_string = input("Please input a string: ")
    print(trimm(trim_string))