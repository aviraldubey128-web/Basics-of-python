detail = {
       "name": "Aviral",
       "age": 19,
       "city": "MP"
}

# adding new key-value pair to the dictionary

detail["country"] = "India"
print(detail)  

# removing a key-value pair from the dictionary

# detail.pop("city")
# print (detail)

detail.keys()
print(detail.keys())

detail.values()
print(detail.values())

detail.items()
print(detail.items())

detail.get("age")
print(detail.get("age"))

detail.update({"city": "new york"})
detail.update({"country": "USA"})
print(detail)

