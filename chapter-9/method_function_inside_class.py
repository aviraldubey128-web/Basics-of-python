class student:
    def __init__(self, name):
        self.name = name
        print(self.name)
s1 = student("aviral")
s2= student("khushi")

class student:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("hello",self.name)
s1 = student("aviral")
s1.hello()