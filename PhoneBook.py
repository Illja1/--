import sys

def add():  
    print('Enter contact info: ')
    dic = {}
    for i in ['Name', 'Last name', 'Number', 'City']:
        dic[i] = input(f'{i}: ')
    print('New contact added')
    return dic

def search_by_name(): 
    srch = input('Search contact by name: ')
    for entry in db: 
        if srch in entry['Name']:
          print(db)

def search_by_last_name(): 
    srch = input('Search contact by last name: ')
    for entry in db:
        
        if srch in entry['Last name']:
          print(db)

def search_by_full_name(): 
    srch = input('Enter contact name: ')
    srch = input('Enter contact last name: ')
    for entry in db:
        
        if srch in entry['Name'] and srch in entry['Last name']:
          print(db)

def search_by_number(): 
    srch = input('Search contact by number: ')
    for entry in db:
        
        if srch in entry['Number']:
          print(db)


def search_by_city(): 
    srch = input('Search contact by city: ')
    for entry in db:
        if srch in entry['City']:
          print(db)

def delete(): 
    search_number = input('Delete contact by number: ')
    i = -1
    while i + len(db) < len(db):
        
        for entry in db:
            if search_number in entry['Number']:
               print(entry)
               db.pop(i)




def update():  # (4)
    search_number = input('Update contact by number: ')
    i = -1
    print(len(db))
    while i + len(db) < len(db):
        
        for entry in db:
            if search_number in entry['Number']:
               print(entry)
               db[i] = add()


def display():  # (optional)
    _ = '- '*40
    print(_)
    for entry in db:
        print(entry)
    print(_+'\n')

def phonebook(name):  # (6)
    import json
    global db
    try:
        with open(f'{name}', 'r') as file:
            db = json.load(file)
            print('Database successfully loaded. Chose option to continue')
    except FileNotFoundError:  # (7)
        if input('Phonebook not found. Any key to create new or [E] to exit: ').lower() == 'e':
            sys.exit("Sometimes it's better stop before you get too far. Goodbye!")
        else:
            print('Phonebook is empty')
            db = [add()]
    while True:
        user_input = input('''\t\t\t\t1-Add
                         2-Search by name
                         3-Search by city
                         4-Search by Last name
                         5-Search by number
                         6-Search by full name
                         7-Delete
                         8-Update
                         9-Exit: ''')
        if user_input == '1': 
          db.append(add())
        elif user_input == '2':  
          search_by_name()
        elif user_input =='3':
          search_by_city()
        elif user_input == '4': 
          search_by_last_name()
        elif user_input == '5':  
          search_by_number()
        elif user_input == '6':  
            search_by_full_name()
        elif user_input == '7':  
          delete()
        elif user_input == '8':
          update()
        elif user_input == '9':
          sys.exit()
          
        with open(f'{name}', 'w') as file:  
            json.dump(db, file, indent=4)


phonebook('phonebook.json')