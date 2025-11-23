# dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values:

d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(d1)
#Dictionary items are ordered, changeable, and do not allow duplicates.
d2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(d2["brand"])
#Duplicate values will overwrite existing values:

d3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(d3)

print(len(d3))

#ou can access the items of a dictionary by referring to its key name, inside square brackets:
d4 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = d4["model"]
print(x)
#The keys() method will return a list of all the keys in the dictionary.
x=d4.keys()
print(x)
#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change