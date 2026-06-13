class python:
    def pay(self):
        print("payment successful!!")

s1 = python()
s1.pay()

class function:
    def __init__(self, bal):
        self.__balance = bal
    def show_balance(self):
        print("balance =", self.__balance)

a1 = function(5000)
a1.show_balance()
