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

# None

def greet():
    print ("Aviral")

result = greet()
print(result)

Aviral
None

# variable scope

x= 10 # this is the global variable

def show():
    x=5 #This is the local variable
    print("Inside the function", x)

show()
print("outhside the fumction", x)

output = '''Inside the function 5
            outhside the fumction 10'''

# parameter and argument 
def greet(name):
    print("hello", name)

greet("Aviral") 

def sum(a,b):
    print("sum=", a+b )

sum(1020302, 3040205)

output = '''hello Aviral
            sum= 4060507'''

# Recursive function 
def factorial(n):
    if  n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

output = '''120'''

# return 

def sum(a,b):
    return a+b
result = sum(223, 2233)
print("Result = ", result)

output = '''Result =  2456'''
