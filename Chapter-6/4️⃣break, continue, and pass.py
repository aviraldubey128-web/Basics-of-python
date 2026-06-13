# break the loop

i = 1
for i in range(1, 13):
    print("iteration", i)
    if i == 12:
        break
    i += 1

# continue the loop

i = 1
for i in range(1, 6):
    if i == 4:
        continue
    print("iteration", i)
    i +=1

# pass the loop

i = 1
for i in range(1,6):
     if i == 4:
         pass
print("iteration", i)
i+=1



