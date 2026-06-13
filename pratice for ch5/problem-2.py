# You are given a list of programming languages:["Python", "Java", "C++", "Python", "Java", "C"]Convert it into a set and print how many unique languages Divya knows.
lan = ["Python", "Java", "C++", "Python", "Java", "C"]
print(type(lan))

lanset = set(lan)
print(type(lanset))

print("how many unique languages Divya knows", len(lanset))

