#a program that prints the sum of first n natural numbers.
n = int(input("enter a number:"))

sum = 0
while n>=1:
    sum = sum + n 
    n = n-1
    print("the sum is", sum)
    print("n", n)