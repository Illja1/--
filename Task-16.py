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




class Product:
    def __init__(self,type,name,price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore(Product):
    