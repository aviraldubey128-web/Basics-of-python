# break the loop

i = 1
for i in range(1, 13):
    print("iteration", i)
    if i == 12:
        break
    i += 1

output =''' iteration 1
iteration 2
iteration 3
iteration 4
iteration 5
iteration 6
iteration 7
iteration 8
iteration 9
iteration 10
iteration 11
iteration 12'''

# continue the loop

i = 1
for i in range(1, 6):
    if i == 1:
        continue
    print("iteration", i)
    i +=1
output = '''iteration 2
iteration 3
iteration 4
iteration 5
'''
# pass the loop

i = 1
for i in range(1,6):
     if i == 4:
         pass
print("iteration", i)
i+=1

output = '''iteration 9''''

