class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self._full_name = full_name
        self._account_number = account_number
        self._routing_number = routing_number
        self._balance = balance


    def deposit(self, amount):
        self._balance = self._balance + amount
        print(f"Amount Deposited: ${amount}")

    def withdraw(self, amount):
        will_it_overdraw = self._balance - amount
        if will_it_overdraw >= 0:
            self._balance = self._balance - amount
            print(f"Amount Withdrawn: ${amount}")
        else:
            self._balance = self._balance - amount - 10
            print("Insufficient Funds. $10 overdraft fee taken out")

    def get_balance(self):
        print(f"Your Balance is: {self._balance}")
        return self._balance

    def add_interest(self):
        interest = self._balance * 0.00083
        return interest

    def print_receipt(self):
        censor = str(self._account_number)[4:8]
        print(self._full_name)
        print(f"Account No.: ****{censor}")
        print(f"Routing No.: {self._routing_number}")
        print(f"Balance: {self._balance}")

person1 = BankAccount("Jake Tanner", 12345678, 81831551, 150.73)
person2 = BankAccount("John Doe", 87654321, 1632152, 05.50)
person3 = BankAccount("Jane Doe", 51234941, 1712562, 650.10)

person1.print_receipt()
person2.get_balance()

person2.withdraw(10)

person3.withdraw(20)
person1.deposit(50)

print(person1.add_interest())
