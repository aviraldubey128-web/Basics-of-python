#a program to print the multiplication table of any number using a while loop.

n = int(input("enter a number:"))
i = n
while i<=10:
    print(f"{i} x {n} = {n*i}")
    i = i+1