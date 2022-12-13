import turtle

class Person:
    def __init__(self,name):
        self.name = name


    

    def activity():

        raise NotImplementedError


class P_U(Person):
    def __init__(self, name):
        super().__init__(name)

    def activity(self):
        
        print(f'{self.name} зараз – красавчег ')


class Zaluzniu(Person):
    def __init__(self, name):
        super().__init__(name)

    def activity(self):
        print(f'{self.name} фахівець по створенню котлів')


class Nevdaha(Person):
    def __init__(self, name):
        super().__init__(name)

    def activity(self):
        print(f'{self.name} Politico: невдаха року')



n1 = P_U('Зеленський')
n2 = Zaluzniu('Залужний')
n3 = Nevdaha('путін')

myList = [n1,n2,n3]

for i in myList:
    i.activity()



class Shape:
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius


    def draw_shape(self):
        raise NotImplementedError("Subbclass...")

    

#class Circle_6(Shape):
#    def __init__(self, x, y, radius,n):
#        super().__init__(x, y, radius)
#        self.n = n


    
class Detail:
    def __init__(self,price):
        self.price = price

    def __add__(self,x):
        if isinstance(self,Detail) and isinstance(x,Detail):
            return 'test'
        else:
            raise TypeError('Invalid')



#a = Detail(200)
#b = Detail(150)
#print(a+2)

def add(product,amount):
    a = list(zip(product,range(len(amount))))
    mydict = {product:amount for product,amount in a}
    print(mydict)

add(('Sport','Football T-Shirt',100),10)