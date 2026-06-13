name = "adda had an apple at NIGHT and got sick"
print(len(name)) # length of the string
print(name.endswith("sick")) # check if the string ends with "sick" and return True or False
print(name.count("a")) # count the number of times "a" appears in the string
print(name.capitalize())
print(name.find("and")) # find the index of the first occurrence of "and" in the string
print(name.replace("adda","harry")) # replace all occurrences of "apple" with "bannana"

print(name.lower())      
print(name.upper())
print(name.strip()) # remove any leading and trailing whitespace from the string
print(name.split()) # split the string into a list of words

# 39
# True
# 7
# Adda had an apple at night and got sick
# 27
# harry had an apple at NIGHT and got sick
# adda had an apple at night and got sick
# ADDA HAD AN APPLE AT NIGHT AND GOT SICK
# adda had an apple at NIGHT and got sick
# ['adda', 'had', 'an', 'apple', 'at', 'NIGHT', 'and', 'got', 'sick']
