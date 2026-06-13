detail = {
       "name": "Aviral",
       "age": 19,
       "city": "MP"
}

# adding new key-value pair to the dictionary

detail["country"] = "India"
print(detail)  
# It will add india in the dictionary
output = {'name': 'Aviral', 'age': 19, 'city': 'MP', 'country': 'India'}

# removing a key-value pair from the dictionary

detail.pop("city")
print (detail)

detail.keys()
print(detail.keys())

output =  dict_keys(['name', 'age', 'city', 'country'])

detail.values()
print(detail.values())

output = dict_values(['Aviral', 19, 'MP', 'India'])

output = 4

detail.items()
print(detail.items())

output = dict_items([('name', 'Aviral'), ('age', 19), ('city', 'MP'), ('country', 'India')])

detail.get("age")
print(detail.get("age"))

Output = 19

detail.update({"city": "new york"})
detail.update({"country": "USA"}) # change the value of country
print(detail)
 output = {'name': 'Aviral', 'age': 19, 'city': 'new york', 'country': 'USA'}

