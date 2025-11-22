n=10
n1="Biomedical engineering"
N="My department is"
n2=345.343
n3=True
a= type(n)
print(a)
print(type(n1)) # hence we can check the python data type
print(type(n3))

#print(type(n,n1,n2,n3)) is not allowed
#ut in list comprehension it is possible and there are also few methods to do that

#write something with the veraible within the print function
print("my department is", n1)

#string to string merging (sane type of daa)
print(N+n1)
# bring the space
print(N+" "+n1)

# if we merge one type of variable with another type than type casting is needed.
n2=str(n2)
print(type(n2))

print(n1 +" "+n2)

#let check the multi-veriable with same name
x=12
x=45
x=3456
print(x) #python always take the updated values. It interprete all the values print the last value





