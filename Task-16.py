import enum
#Task-1

class Pesron():
    def __init__(self,name,surname,age,character):
        self.name = name
        self.surname =  surname
        self.age = age
        self.character = character
        print(f'{name},{surname},{age},{character}')

class Student(Pesron):
    def __init__(self,name,surname,age,excellent_student,character,c_be_teacher):
        super().__init__(self,name,surname,age,character)
        self.excellent_student = excellent_student
        self.c_be_teacher = c_be_teacher
        print(f'{name},{surname},{age},{excellent_student},{c_be_teacher}')

    def do_homework(name,surname,age,excellent_student,character,c_be_teacher):
        if excellent_student == True:
            print(f'{name},{surname},{age},{excellent_student},{c_be_teacher}')
            print('Yes')
        else:
            print(f'{name},{surname},{age},{excellent_student},{c_be_teacher}')
            print('No')

class Teacher(Pesron):
    def __init__(self,name,surname,age,character,sallary,teacher,work_day_end):
        super().__init(self,name,surname,age,character,sallary)
        self.sallary = sallary
        self.teacher = teacher
        print(f'{name},{surname},{age},{sallary},{teacher}')

    def check_homework(name,surname,age,character,sallary,teacher,work_day_end):
        if work_day_end == True:
            print(f'{name},{surname},{age},{character},{teacher},{work_day_end}')
            print('Yes')
        else:
            print(f'{name},{surname},{age},{character},{teacher},{work_day_end}')
            print('No')



Pesron('Illja','Homenko',18,'good')
Student.do_homework('Illja','Homenko',18,True,'good',False)
Teacher.check_homework('Illja','Homenko',40,'bad',4600,True,False)

#Task-2

class Mathematician:

    def square_nums(self,*args):
        for x in args:
            print([y**2 for y in x])

    def remove_positives(self,*args):
        for x in args:
            print([y for y in x if y <= 0])
    
    def filter_leaps(self,*args):
        for x in args:
            print([y for y in x if  y%4 ==0 and y%100 != 0 or y%400 == 0])


m = Mathematician()

m.square_nums([7, 11, 5, 4]) 

m.remove_positives([26, -11, -8, 13, -90]) 

m.filter_leaps([2001, 1884, 1995, 2003, 2020]) 



#Task-3
class Product:
    def __init__(self,type,name,price)->list:
        self.type = type
        self.name = name
        self.price = price+30

 

    def __str__(self):
            return f"{self.type,self.name,self.price}"
        

    def __repr__(self):
            return self.__str__()



class ProductStore():
    def __init__(self):
        self.db= {}


    def add(self,product,amount):
        self.db.update({product:amount})


    def set_discount(self,identifier, percent, identifier_type='name'):
        q = percent/100
        for i in self.db:
            if identifier == i.type and identifier_type == i.name:
                x = i.price*q
                price_with_disc = i.price-x

                print(f'New price of {i.name}: {price_with_disc}')


    def sell_product(self,product_name, amount):
        for value in self.db.values():
            for i in self.db:
                if product_name == i.name:
                    new_amount = value-amount
        print(f'New amount of {i.name}: {new_amount}')


    def get_income(self):
        x = 0
        for i in self.db:
            x = i.price+x   
        print(f'Income: {x}')


    def get_all_products(self):
        print(self.db)


    def get_product_info(self,product_name):
        for i in self.db:
            if product_name == i.name:
                print(f'All info about product: {i.type}-{i.name}-{i.price}')
    







p = Product('Sport','Football T-Shirt',100)
p1 = Product('Food', 'Ramen', 20)
p2 = Product('Sport', 'Ball', 50)
s = ProductStore()
s.add(p,10)
s.add(p1, 300)
s.add(p2, 200)
s.set_discount('Sport',10,'Football T-Shirt')
s.set_discount('Food',20,'Ramen')
s.set_discount('Sport',5,'Ball')
s.sell_product('Ramen',10)
s.sell_product('Ball',99)
s.sell_product('Football T-Shirt',8)
s.get_income()
s.get_all_products()
s.get_product_info('Football T-Shirt')
s.get_product_info('Ramen')
s.get_product_info('Ball')


#Task-4

class CustomExceptoin(Exception):
    def __init__(self,error,message):
        self.error = error
        self.message = message
        message = error
        super().__init__(self.message)
        with open('log.txt','a+') as f:
            f.write(self.message)


#sallary = int(input('Enter sallary: '))
#if not 5000< sallary < 15000:
#    raise CustomExceptoin(sallary,message='Invalid range')   



