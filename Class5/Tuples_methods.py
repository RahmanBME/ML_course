#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.Tuples are written with round brackets.
#example
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Tuple items are ordered, unchangeable, and allow duplicate values.
t1 = ("apple", "banana", "cherry", "apple", "cherry")
print(t1)
#length of tuople
tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(len(tuple1))

#one item tuple

t1=("grape sugar",)#this is tuple not string.
print(type(t1))
t1=("grape sugar")
print(type(t1))# this is string

#tuple can cotain any types of data
t2=("sag",34,True,"female")
print(type(t2))

#Access tuple\
t2=("sag",34,True,"female")
print(t2[1])
print(t2[-2]) #negative indexing
#range in tuple as like list
t3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t3[2:6])
print(t3[:4])
print(t3[2:])

#check the item
if "luchi" in t3:
    print("yes")
else:
    print("no")

#upadate tuples
#this is unchangeble. to chang the item, tuple has to be converted into list tha n chane the value and reconvert to tuple

t4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
l1=list(t4)
l1[1]="grape sugar"
t4=tuple(l1)
print(t4)

#tuple allow to add one with another
t5 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
t6= ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
t7=t5+t6
print(t7)

#the loop in tuple is as like as list





