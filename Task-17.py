#Task-1
class Animal:
    def talk():
        raise NotImplementedError




class Dog(Animal):
    def talk():
        print('Wof-Wof')



class Cat(Animal):
    def talk():
        print('Meow')


def u_input():
    user_input = input('Enter class: ')
    if user_input == 'Dog':
        Dog.talk()
    elif user_input == 'Cat':
        Cat.talk()



#u_input()


#Task-2
class Library:
    def __init__(self,name) -> None:
        self.name= name
        self.books = []
        self.authors = []

    def new_book(self,name,year,author):
        new_book = Book(name,year,author)
        self.books.append(new_book)
        self.authors.append(author)
        Book.a_books += 1
        return new_book
    
    def group_by_author(self,author):
        for i in self.books:
            if i.authors == author:
                return i.name,i.year

    def group_by_year(self,year):
        for i in self.books:
            if i.year == year:
                print('Test')
    def __repr__(self) -> str:
        return f'{self.name}, {self.books}, {self.authors}'

    


class Book:
    a_books = 0

    def __init__(self,name,year,author):
        self.name= name
        self.year = year
        self.authors = author

    def __repr__(self) -> str:
        return f'{self.name}, {self.year}, {self.authors}'

    def __str__(self) -> str:
        return f'{self.name}, {self.year}, {self.authors}'


class Author:
    def __init__(self,name,country,bh):
        self.name = name
        self.country = country
        self.bh = bh
        self.books = []

    def __repr__(self) -> str:
        return f'{self.name}, {self.country}, {self.bh}'

    def __str__(self) -> str:
        return f'{self.name}, {self.country}, {self.bh}'



#Task-4
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

    def __str__(self):
         return str(self.num)+"/"+str(self.den)

    def show(self):
         print(self.num,"/",self.den)

    def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)
    
    def __sub__(self,otherfraciton):
        newnum = self.num*otherfraciton.den - self.den*otherfraciton.den
        newden = self.den * otherfraciton.den

        common = gcd(newnum,newden)

        return Fraction(newnum//common,newden//common)

    def __mul__(self,other):
        newnum = self.num * other.num
        newden = self.den + other.den

        common = gcd(newnum,newden)

        return Fraction(newnum//common,newden//common)    

    def __truediv__(self,other):
        newnum = self.num * other.den
        newden = self.den + other.num

        common = gcd(newnum,newden)

        return Fraction(newnum//common,newden//common)    

        


x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)