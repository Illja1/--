class Car:
    def __init__(self,mark,model,km,price) -> None:
        self.mark = mark
        self.model = model
        self.km = km
        self._price = price

    def getx(self):
            return self.mark,self.model,self.km,self._price

    def setx(self, price):
            self._price = price
            return 

    def delx(self):
            del self.mark 
            del self.model 
            del self.km
            del self._price 

    my_property  = property(getx, setx, delx, "I'm the 'x' property.")


#p = Car('Toyota','Corola',200000,30000)

#del p.my_property
#print(p.my_property)


class Car:
    def __init__(self,mark,model,km,price) -> None:
        self.mark = mark
        self.model = model
        self.km = km
        self._price = price
    @property
    def myprice(self):
            return self.mark,self.model,self.km,self._price
    @myprice.setter
    def myprice(self, price):
            self._price = price
            return 

    @myprice.deleter
    def myprice(self):
            del self.mark 
            del self.model 
            del self.km
            del self._price 

    
class Client:
    def __init__(self,full_name,bal) -> None:
          self._full_name = full_name
          self.bal = bal
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self,new):
        if isinstance(new,str):
            x = new.split(' ')
            if len(x) == 3:
                print(new)

            else:
                raise Exception


p = Client('Illja Homenko',200)

p.full_name = 'Illja Homenko'
