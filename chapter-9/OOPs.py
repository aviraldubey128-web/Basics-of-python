class student:
    name = "aviral"
    age = "19"
    DOB = "01/02/20XX"
    
s1 = student()
s2 = student()
s3 = student()
print(s1.name)
print(s2.age)
print(s3.DOB)

output = '''aviral
        19
        01/02/20XX'''

-Method_function_inside_class 

class student:
    def __init__(self, name):
        self.name = name
        print(self.name)
s1 = student("aviral")
s2= student("vivek")

class student:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("hello",self.name)
s1 = student("aviral")
s1.hello()
class students:
    def hello(self):
        print('hello', self.name)
s2 = student('vivek')
s2.hello()

output = '''aviral
            vivek
            hello aviral
            hello vivek'''

-Static method
class student:
    @staticmethod
    def school():
        print("abc")

student.school()

output = '''abc'''

- Instance attributs

class Student:
    college = "XYZ Institute"

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")
        print(f"College: {self.college}")

s1 = Student("Aviral")
s1.display()

output = '''Name: Aviral
            College: XYZ Institute'''

-abstraction & Encapslation
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

output = '''payment successful!!
            balance = 5000'''

-Indheritance $ polymorphism

class vehicle:
    def start(self):
        print("Vehicle is starting")

class car(vehicle):
    def start(self):
        print("car is now moving")

class bike(vehicle):
    def ride(self):
        print("bike isnow riding")

class truck(vehicle):
    def load(self):
        print("Truck is loading")

c = car()
c.start()
b = bike()
b.ride()
t = truck()
t.load()

output = '''car is now moving
            bike isnow riding
            Truck is loading'''
polymorphism

class dog:
    def sound(self):
        print("dog will: bark")

class cat:
    def sound(self):
        print("cat will: meow")


class cow:
    def sound(self):
        print("cow will: moo")

animal = [dog(), cat(), cow()]
for a in animal:    
    a.sound()

output'''dog will: bark
cat will: meow
cow will: moo'''


