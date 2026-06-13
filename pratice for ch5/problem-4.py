# Create a set of numbers and show union and intersection with another set.

set1 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
set2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

set1.union(set2)
print(set1.union(set2))

elt1 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
elt2 = {1 , 2, 3, 5, 7, 11, 13, 17, 19 }

elt1.intersection(elt2)
print(elt1.intersection(elt2))