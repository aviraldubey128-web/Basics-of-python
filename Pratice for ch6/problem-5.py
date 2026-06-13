# a program to print this pattern using a while loop: 
# *
# * *
# * * *
# * * * *
n = (int(input("enter a number:")))
i = 1
while i<=n:
    print("* "*i)
    i = i+1
    j = 1
    while j<=i:
        print("* ", end="")
        j = j+1
    print()  # Move to the next line after each row