#A set is a collection which is unordered, unchangeable*, and unindexed.
#but set is mutable

s1 = {"apple", "banana", "cherry"}
print(s1)

#Duplicates Not Allowed
s2 = {"apple", "banana", "cherry", "apple"}

print(s2)
#set may contain anytype of data and lemgth can be calculated using len()
# the data type of set is set
#it is not like the list, you can not run several operation like the list
# one set can be added with another set

S3=s1 | s2
print(S3) #dose not allow duplicate value

s4 = {"apple", "banana", "cherry"}

s4.remove("banana")

print(s4)