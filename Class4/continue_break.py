n3=10
for x in range(n3):
    if x==5:
        break
    print("abdur rahman",x)

#continue
n3=10
for x in range(n3):
    if x==5:
        continue  # continue is one type of skip
    print("abdur rahman", x)

#range with artribur( start, end and step
for x in range(2,7,3): # 2 is start, 7 is end, 3 is step

    print(x)
n4="banana"
for x in n4:
    if x=="n":
        continue
    print("gold",x)


n5="apple","banana","luchi","rellish","cabbage"
for x in n5:
    if x=="banana":
        print("this test is bad",x)
        continue
    print(x)


fruits="apple","luchi","banana"
for x in fruits:
    print(x)
    if x=="luchi":
        break
    print(x)
