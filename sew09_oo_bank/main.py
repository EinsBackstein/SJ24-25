from accounts import CheckingAccount, SavingAccount
from controller import Bank

bank = Bank()

def menu():
    print("\n\n\n")
    print("1. Create a new account")
    print("2. Check account")
    print("3. Check all accounts")
    print("4. Do accounting")
    print("5. Deposit")
    print("6. Withdraw")
    print("0. Exit")
    print("\n")
    choice = input("Enter your choice: ")
    return choice

def checks(account_type = None,account_number = None, balance = None, bank=bank, fee = None, interest_rate = None):
    if(account_type != "checking" and account_type != "saving" and account_type != None):
        print("Invalid account type")
        return False
    if account_number in bank.get_accounts() and account_number != None:
        print("Account already exists")
        return False
    if(type(balance) != float and balance != None):
        print("Invalid balance")
        return False
    if(balance != None):
        if(balance < 0 and balance != None):
            print("Balance cannot be negative")
            return False
    if(type(fee) != float and fee != None):
        print("Invalid fee")
        return False
    return True

def main():
    while True:
        choice = menu()
        if choice == "1":
            account_type = input("Enter account type (checking/saving): ")
            if checks(account_type) == False: continue
            account_number = input("Enter account number: ")
            if checks(None,account_number) == False: continue
            balance = float(input("Enter balance: "))
            if checks(None,None,balance) == False: continue
            if account_type == "checking":
                fee = float(input("Enter fee (€): "))
                if checks(None,None,None,None,fee) == False: continue
                account = CheckingAccount(account_number, balance, fee)
            elif account_type == "saving":
                interest_rate = float(input("Enter interest rate (%): "))
                if checks(None,None,None,None,None,interest_rate) == False: continue
                account = SavingAccount(account_number, balance, interest_rate)
            bank.add_account(account)
        if choice == "2":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account == None:
                print("Account not found")
            else:
                print(account)



if __name__ == "__main__":
    main() 