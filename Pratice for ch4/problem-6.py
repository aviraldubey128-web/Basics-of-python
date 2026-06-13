# a program to check grade based on marks (A/B/C/D) using if-elif-else.

marks = int(input("Enter the marks of the student:"))
if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: D")
