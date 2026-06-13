# class Student with name, class, marks. Add method get_percentage().
class Student:
    def __init__(self, name, student_class, marks):
        self.name = name
        self.student_class = student_class
        self.marks = marks

    def get_percentage(self):
        percentage = (self.marks / 100) * 100
        return percentage


# Creating object
s1 = Student("Aviral", "12th", 85)

print("Name:", s1.name)
print("Class:", s1.student_class)
print("Marks:", s1.marks)
print("Percentage:", s1.get_percentage(), "%")