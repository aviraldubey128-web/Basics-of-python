# class Student that takes 3 marks and has a method average().
class student():
        def __init__(self,m1,m2,m3):
                self.m1 = m1
                self.m2 = m2
                self.m3 = m3
        
        def average(self):
                avg = (self.m1 + self.m2 + self.m3)/3
                return avg
        
s1 = student(133,334,344)
print("Average marks=", s1.average())