#access list
list = ["apple", "banana", "cherry"]
print(list[1])
#negative indexing
list = ["apple", "banana", "cherry"]
print(list[-1])
#Return the third, fourth, and fifth item:

list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[2:5])
print(list[:4])

#use of if condition
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in list:
    print("yes")
else:
    print("no")

#change the value using index
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list[0:3]=["banana", "mango"]
print(list)

#insert item in list

list1= [ "banana", "cherry", "orange", "kiwi", "melon", "mango"]
(list1.insert(3,"cabbage"))
print(list1)
(list1.insert(-2,"cabbage"))
print(list1)

#append method. It add the item at end

list1= [ "banana", "cherry", "orange", "kiwi", "melon", "mango"]

list1.append("banana")
print(list1)

#pop methof( delete using index)
list1= [ "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list1.pop(1) # the cherry will be removed

print(list1)
#del list1 #list1 will be removed

#print(list1)

list1= [ "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#use of clear function
list1.clear() #empty lsit will be shown

print(list1)

#loop run in list
list1= [ "banana", "cherry", "orange", "kiwi", "melon", "mango"]


for i in range(len(list1)):

    print(list1[i])
#use of range function
list1= [ "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for i in range(len(list1)):
    if i%2==0:
        continue
    print(list1[i])

#empty list
list1= [ "banana", "cherry", "orange", "kiwi", "melon", "mango"]
my_list=[]
for x in list1:
    if "a" in x:
        my_list.append(x)
print(my_list)


#joint method is like concatenate
list1= [ "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list2=["banana", "cherry", "orange", "kiwi", "melon", "mango"]
list3=list1+list2
print(list3)
#there are other methods like short, copy etc in list
