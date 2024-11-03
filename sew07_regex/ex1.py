import re


def validate_phone_number(phone_number):
    # Explanation of the regex pattern:
    # \+?              # Matches an optional "+" at the beginning, often used for international dialing.
    # (\d{1,3})        # Matches 1 to 3 digits (usually the country code) and groups them together.
    # [-./ ]?          # Matches an optional separator: a dash, dot, slash, or space.
    # [(]?             # Matches an optional opening parenthesis (for area code).
    # \d{1}?           # Matches 0 or 1 digit inside the parentheses (some formats have a single digit in parentheses).
    # [)]?             # Matches an optional closing parenthesis.
    # \(?\d{0,4}\)?    # Matches 0 to 4 digits, optionally enclosed in parentheses (used for area codes).
    # [-./ ]?          # Matches an optional separator after the area code.
    # \d{0,7}          # Matches 0 to 7 digits (main part of the phone number).
    # [-. ]?           # Matches an optional separator.
    # \d{0,4}          # Matches 0 to 4 additional digits.
    # [-. ]?           # Matches an optional separator.
    # \d{0,2}          # Matches 0 to 2 digits at the end.
    pattern = r'^\+?(\d{1,3})[-./ ]?[(]?\d{1}?[)]?\(?\d{0,4}\)?[-./ ]?\d{0,7}[-. ]?\d{0,4}[-. ]?\d{0,2}$'
    return bool(re.fullmatch(pattern, phone_number))


list = {
    "+43 664 1234 567",
    "0650/5130764",
    "0043 4242 12345",
    "+43 (0)676 765 4382 12"
}


if __name__ == "__main__":
    for item in list:
        print(f"Phone Number: {item} is valid: \n{
              validate_phone_number(item)}\n")
