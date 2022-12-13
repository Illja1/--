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
    
class Author():
    def __init__(self,first_name,country,date,books) -> None:
        self.first_name = first_name
        self.coutry = country
        self.date = date
        self.books = books



class Book(Author):
    def __init__(self, first_name, country, date, books,book_name,year,author) -> None:
        super().__init__(first_name, country, date, books)
        self.book_name = book_name
        self.year = year
        self.author = author



class Library(Book):
    def __init__(self, first_name, country, date, books, book_name, year, author) -> None:
        super().__init__(first_name, country, date, books, book_name, year, author)
    


    def new_book(book_name,year,author):
        global mylist
        mylist = {"Book name":book_name,'Year':year,'Author': author}
        print('Book added')
        print(mylist)
    
        #print(mylist)

    def group_by_author():
        srch = input('Search book by name: ')
        for entry in mylist: 
            if srch in entry['Author']:
                print(mylist)

    def display():
        for i in mylist:
            print(mylist)


Library.new_book('test',1999,'Jake')
Library.new_book('test-1',2000,'Mike')
Library.new_book('test-2',1999,'Jake')
Library.display()



class MyNum:
    def __init__(self, value,value1):
        self.value = value
        self.value1 = value1

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError
        return MyNum(self.value+other.value)

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError
        return MyNum(self.value-other.value)

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError
        return MyNum(self.value*other.value)

    def __truediv__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError
        return MyNum(self.value/other.value)
   
    
    def __str__(self):
        return f"<MyNum: {self.value}>"
    
    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    x = MyNum(1,2)
    y = MyNum(1,4)
    #c = MyNum(2)
    #v =MyNum(4)
    #print(x*c)
    #print(y*v)
    print(x+y)






