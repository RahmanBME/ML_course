'''List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.'''
list=['apple','banana','luchi','orange']
print(list)
'''
Characteristics of a List

Ordered – Elements follow a specific sequence.

Mutable – You can change, add, or remove items.

Allows duplicates – Same value can appear multiple times.

Stores multiple data types – Can contain int, float, string, list, etc.

Dynamic size – Size can grow or shrink anytime.

Indexed – Items can be accessed using index numbers.'''

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

#data type of list

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#list value change

fruits = ["apple", "banana", "cherry"]
fruits[0]= "kiwi"

print(fruits)


n= ("banana","luchi","orange")
x=list(n)
print(type(x))






