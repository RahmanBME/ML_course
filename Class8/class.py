class baba():
    car='bme'
    tk='100cr'

#inheritance
class ma(baba):
    h=100
    tk1=200

z=ma()
print(z.tk1)
print(z.car)

class kaka(ma,baba):
    pass
y=kaka()
print(y.tk1)


class me():
    def junaid(self,a,b):
        print(a+b)




#x=me()
#x.junaid(20,30)

class babu():
    def __init__(self, a,b):
        print(a+b)

b=babu(10, 14) #magic method




