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
        Book.a_books = +1
        return new_book
    
    def group_by_author(Self,author):
        return author.books

    def group_by_year(self,year):
        pass

    def __repr__(self) -> str:
        return f'{self.name}, {self.books}, {self.authors}'

    


class Book:
    a_books = 0

    def __init__(self,name,year,author) -> None:
        self.name= name
        self.year = year
        self.authors = author

    def __repr__(self) -> str:
        return f'{self.name}, {self.year}, {self.authors}'

    def __str__(self) -> str:
        return f'{self.name}, {self.year}, {self.authors}'


class Author:
    def __init__(self,name,country,bh) -> None:
        self.name = name
        self.country = country
        self.bh = bh
        self.books = []

    def __repr__(self) -> str:
        return f'{self.name}, {self.country}, {self.bh}'

    def __str__(self) -> str:
        return f'{self.name}, {self.country}, {self.bh}'


author_1 = Author('Test','test','29.04.1994')
author_2 = Author('Test-1','test-1','30.08.1995')
lib = Library('Slavuta library')
print(lib.new_book('name1',1999,author_1))
print(lib.new_book('name2',1995,author_2))
print(lib.new_book('name3',1999,author_1))
print(lib.new_book('name4',2000,author_2))
print(Book.a_books)
print(author_1.books)
print(author_2.books)
print(lib.group_by_author(author_1))
print(lib.group_by_author(author_2))
print(lib.group_by_year(1999))


   




class MyNum:
    def __init__(self, value,value1):
        self.value = value
        self.value1 = value1


    def __add__(self, other,value1):
        if not isinstance(other,value1, type(self)):
                raise ValueError
        else:
            r = MyNum(self.value+self.value)
            r_1 = MyNum(other.value+other.value1)

        def __str__(self):
            return f"<MyNum: {self.value+self.value1}>"
        
        def __repr__(self):
            return self.__str__()

    def __sub__(self, other,value1):
        if not isinstance(other,value1, type(self)):
                raise ValueError
        else:
            r = MyNum(self.value+self.value)
            r_1 = MyNum(other.value-other.value1)
        
    
        def __str__(self):
            return f"<MyNum: {self.value-self.value1}>"
        
        def __repr__(self):
            return self.__str__()

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError

        def __str__(self):
            return f"<MyNum: {self.value*self.value1}>"
        
        def __repr__(self):
            return self.__str__()

    def __truediv__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError

        def __str__(self):
            return f"<MyNum: {self.value/self.value1}>"
    
        def __repr__(self):
            return self.__str__()


if __name__ == "__main__":
    x = MyNum(1,2)
    y = MyNum(1,4)
    print(x)
    print(y)
   # print(x+y)
#   print(x+y==MyNum(3,4))






