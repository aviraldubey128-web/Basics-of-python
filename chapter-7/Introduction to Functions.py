#functions def

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
d = int(input("Enter the fourth number:"))
e = int(input("Enter the fifth number:"))
f = int(input("Enter the sixth number:"))
# This wil certainly reduce the readablity of code 
# to avoid this we use parameter and arugment

output = Enter the first number:123
Enter the second number:322
Enter the third number:212 
Enter the fourth number:322
Enter the fifth number:212
Enter the sixth number:322
def sum():
    print("THE SUM OF a & b", a+b)
sum()

output = '''THE SUM OF a & b 445'''

def product():
    print("THE PRODUCT OF c & d", c*d)
product()

output = '''THE PRODUCT OF c & d 68264'''

def division():
    print("THE DIVISION OF e AND f", e/f)
division()

output = '''THE DIVISION OF e AND f 0.6583850931677019'''

# defaut argument
def greet(name = "aviral"):
    print("Hello there,", name)

greet("saumya")
greet()

output = '''Hello there, saumya
Hello there, aviral '''
