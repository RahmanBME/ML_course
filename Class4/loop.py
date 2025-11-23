#A loop is a programming concept that lets you repeat the same task again and again without writing the code many times.

n="bangladesh"
z=0


print(n)
for x in n:
    z+=1
    print(z) #according to the lemgth of the n, z will be printed
    print(x)

print(z) # only the total value of z will be printed

# lets define a new variable
n1="bangladesh","india","pakistan"
y=0
for x in n1:
    y+=1
    print(x)

#use of range function. it is for numerical value

n2=10
for x in range(n2):
    print("abdur rahman", x)


n3=10
for x in range(n3):
    if n3==5:
        break
    print("abdur rahman", x)




