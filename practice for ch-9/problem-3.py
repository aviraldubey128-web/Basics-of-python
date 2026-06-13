#a class FoodItem with class attribute category = "Snacks" and instance
#attribute name (“Samosa”, “GulabJamun”).

class fooditem():
    category = "Snacks"
    def __init__(self, name):
        self.name = name

i1 = fooditem("samosa")
i2 = fooditem("gulabjammun")

print(i1.name,"-", i1.category)
print(i2.name,"-", i2.category)

