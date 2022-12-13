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
    def __init__(self,type,name,price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        pass

    def add(self,product,amount=0):
         



    #def get_product_info(self,product_name):
    #    if product_name == mydict.keys():
    #        print(product_name)
    #    else:
    #        print('Product not found')






p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.get_product_info('Ramen')


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



