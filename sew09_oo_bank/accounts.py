from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number: str, balance: float):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
    
    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    @abstractmethod
    def do_accounting():
        pass
    
    def __str__(self) -> str:
        return f"Account {self._account_number}: Balance {self._balance}€"

    def __eq__(self, other) -> bool:
        if not isinstance(other, BankAccount):
            return ValueError("Not same instance")
        return self._account_number == other.account_number


class SavingAccount(BankAccount):
    def __init__(self, account_number: str, balance: float, interest_rate: float):
        if interest_rate <= 0:
            raise ValueError("Interest rate must be positive.")
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self) -> float:
        return self._interest_rate

    def do_accounting(self):
        self._balance += self._balance * (self._interest_rate / 100)


class CheckingAccount(BankAccount):
    
    def __init__(self, account_number: str, balance: float, fee: float):
        if fee < 0:
            raise ValueError("Fee cannot be negative.")
        super().__init__(account_number, balance)
        self._fee = fee

    @property
    def fee(self) -> float:
        return self._fee

    def do_accounting(self):
        self._balance -= self._fee