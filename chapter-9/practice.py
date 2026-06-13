class amount:
    def __init__ (self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def credit(self, amount):
            self.balance += amount
            print("Amount credited:", amount)

    def debit(self, amount):
            if amount <= self.balance:
                self.balance -= amount
                print("Amount debited :", amount)
            else:
                print("Insufficient fund")
    def show_balance(self):
            print("amount:", self.account_number ,"| balance:", self.balance)
              
a1 = amount(10000, 5000)
a1.credit(2000)
a1.debit(20000)
a1.show_balance()
