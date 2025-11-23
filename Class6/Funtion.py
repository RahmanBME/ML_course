'''A function is a block of organized, reusable code that performs a specific task.
Functions help avoid repeating code and make programs more modular and readable.'''

def abdur_rahman():
    print("hellow")


abdur_rahman()

def rana():
    n=int(input("enter your number"))
    for x in range(n):
        print(x)

rana()

#argument pass in function
def sum(x,y):
    print(x+y)

sum(10,20)

def sum(x,y):
    return x+y

print(sum(10,20))

print(sum(10,20)-10)


# tuple set in funciton

def babu(*x):
    return x
print(babu(10,11,12,12,13))

n=10
def fun():
    n1=50
    print(n+n1)
fun()
print(n+50) #local variable can not be used


#lamda function
n=lambda a,b: a+b +10
print(n(12,34))



