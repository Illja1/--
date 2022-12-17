#Task-1
import re
class Check:

    def __init__(self,email):
        type(self).validate(email)
        self.email = email


    @classmethod
    def validate(cls, email):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise TypeError(f'Email {email} is invalid')


email1 = Check('test@gmail.com')
email2 = Check('Illja2004@mail.com')
#email3 = Check('Johnygmail.com')
#email4 = Check('illja.com')

#Task-2
class Boss:
    def __init__(self,id_:int,name:str,company:str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []
        


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss


b = Boss(1,'Dima','Twrl')

#Task-3
class TypeDecorators:
    def to_int(foo):
        def __int__(string):
            x = foo(string)
            print(x)
        return __int__

    def to_bool(foo):
        def magic(self):
            print(bool(foo(self)))
        return magic


    def to_str(foo):
        def magic(self):
            print(foo(self))
        return magic

    def to_float(foo):
        def magic(self):
            print(float(foo(self)))
        return magic


@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

print(type(do_nothing('25')))
do_something('True') == True
