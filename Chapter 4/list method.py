items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
items.append("king") # This will add the word at the end of the list, so the list will now be ["Apple", "Banana", "Cherry", "Date", "Elderberry", "king"]
print(items)
# ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'king']
items.insert(1, "graphs") #this will insert the word "graphs" at index 1, so the list will now be ["Apple", "graphs", "Banana", "Cherry", "Date", "Elderberry", "king"]
print(items)

# ['Apple', 'graphs', 'Banana', 'Cherry', 'Date', 'Elderberry', 'king']

l1 = ["m", "p", "h", "c", "a", "o", "q", "r", "z", "i"] 
l1.sort()
print(l1)

# l1: ['a', 'c', 'h', 'i', 'm', 'o', 'p', 'q', 'r', 'z']

l2 = ["100", "200", "300", "400", "500", "600", "700", "800", "900", "1000"]

l2.reverse() # this will reverse the order of the list 
print(l2)

# l2 ['1000', '900', '800', '700', '600', '500', '400', '300', '200', '100']

l3 = ["pen", "paper ", "book", "notebook", "pencil", "eraser", "sharpener", "ruler", "stapler", "scissors"]

print(l3.pop(2)) # this will remove the item from the index
#  book
print(l3)

# l3 ['pen', 'paper ', 'notebook', 'pencil', 'eraser', 'sharpener', 'ruler', 'stapler', 'scissors']

l4 = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"]

l4.insert(5, "cyan")
l4.insert(3, "magenta") #this will instert the word "magenta" at index 
print(l4)
# l4 ['red', 'blue', 'green', 'magenta', 'yellow', 'orange', 'cyan', 'purple', 'pink', 'brown', 'black', 'white']
