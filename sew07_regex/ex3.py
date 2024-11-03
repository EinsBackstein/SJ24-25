import re

def check_password_strength(password):
    # (?=.*[a-z]) - At least one lowercase letter
    # (?=.*[A-Z]) - At least one uppercase letter
    # (?=.*\d) - At least one digit
    # (?=.*[@$!%*?&]) - At least one special character
    # {8,} - At least 8 characters
    pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}'
    return bool(re.fullmatch(pattern, password))


list = {
    "Passw0rd!",
    "weakpwd",
    "1234567890",
    "STRONGPASSWORD123"
}

if __name__ == "__main__":
    for password in list:
        print(password, check_password_strength(password))
