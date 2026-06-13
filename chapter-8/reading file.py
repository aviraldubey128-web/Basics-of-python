# Read wntire file
with open("python note 3.txt", "r") as f:
    data = f.read()
    print(data)

# Read line by line
with open("hello_to_world.txt", "r") as f:
    line1 = f.readline()
    print("Line 1:", line1)
    
    

# Read all the lines
with open("hello_to_world.txt","r") as f:
    lines=f.readlines()
    print(lines)




