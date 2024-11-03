import re

def validate_phone_number(phone_number:str):
    #Explanation of the regex pattern:
    #^\+?(\d{1,3}) - Beginning of Phone Number, Optional +, 1-3 Digits (e.g. +43)
    #?[-. ] - Separator (e.g. - or . or Space)
    #?\d{3} - String of 3 Numbers
    #?\d{4} - String of 4 Numbers
    pattern = r"^\+?(\d{1,3})?[-. ]?\d{3}?[-. ]?\d{4}[-. ]?\d{4}$"
    return bool(re.fullmatch(pattern, phone_number))


if __name__ == "__main__":
    print(validate_phone_number("+43 676 1234 1234"))