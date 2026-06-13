 #a program to accept marks of 6 students and display them in a sorted manner

marks = []
for i in range(6):
    marks.append(int(input("Enter the marks of student {}: " .format(i+1) )))       
    marks.sort()
    print("the marks of the students in sorted manner are:", marks)

    



