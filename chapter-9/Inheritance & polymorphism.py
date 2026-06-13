# Inheritance
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

# polymorphism

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