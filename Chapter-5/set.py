elt = {"apples", "bananas", "cherries", "apples", "cherries"}
print(type(elt))

print(elt)
<class 'set'>
{'cherries', 'apples', 'bananas'}

## Set methods:

elt = {"apples", "bananas", "graphs", "apples", "graphs"}
elt2 = {"grapes", "apples", "pears", "grapes", "pears"}

elt.add("5")
print(elt)

output = {'5', 'apples', 'bananas', 'graphs'}

elt.union(elt2)
print(elt.union(elt2))

output = {'apples', 'graphs', '5', 'grapes', 'pears', 'bananas'}

elt.intersection(elt2)
print(elt.intersection(elt2))

output = {'apples'}

elt.remove("cherries")
print(elt)

output = {'5', 'apples', 'graphs'}
