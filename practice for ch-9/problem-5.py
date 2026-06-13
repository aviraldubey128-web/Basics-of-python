#Create static method to validate if a number is even.
class number:
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"


print(number.is_even(22))
print(number.is_even(120322))
          
        