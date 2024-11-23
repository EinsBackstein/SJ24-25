from accounts import BankAccount, CheckingAccount, SavingAccount

class Bank:
    def __init__(self):
        self._accounts: list[BankAccount] = []

    def add_account(self, account: BankAccount):
        if account in self._accounts:
            raise ValueError("Account already exists")
        self._accounts.append(account)

    def get_account(self, account_number: str):
        for account in self._accounts:
            if account.account_number == account_number:
                return account
        return None
    
    def get_accounts(self):
        accounts = []
        for account in self._accounts:
            accounts.append(account.account_number)
        return accounts
    
    def do_accounting(self) -> None:
        for account in self._accounts:
            account.do_accounting()