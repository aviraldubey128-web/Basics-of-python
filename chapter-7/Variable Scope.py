x= 10 # this is the global variable

def show():
    x=5 #This is the local variable
    print("Inside the function", x)

show()
print("outhside the fumction", x)