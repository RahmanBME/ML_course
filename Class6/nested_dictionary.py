#nested list
list=[[1,2,3],[4,5,6],[7,8,9]]
print(len(list))

#nested dictionary
n={"name":"abdur rahman","age":26}
n1={"man1":{"name":"rana",
            "age":25},
    "man2":{"name":"robi",
            "age":23
            }
    }
print(n1)
print(n1["man1"])
print(n1["man2"]["age"])

print(len(n1)) #length of the decitonary
print(n1.keys())


#loop

for x,y in n1.items():
    print(x,y)

