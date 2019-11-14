def chek_admin(person_id): #Проверяет, является ли человек админом или нет (admin, member or none)
    person = 'none'
    
    f = open('data/admin.csv')
    admin_id = f.read().split(',')[0]
    f.close()
    
    with open('data/members.csv') as file:
        for person_str in file:
            person_array = person_str.split(',')
            if person_array[0] == str(person_id):
                person = 'member'
    
    if str(person_id) == admin_id:
        person = 'admin'
        
    return person

def insert_register(message, person_id): #записывает в бд имя(инфу) по id
    f = open('data/members.csv', 'r')
    members_array = list(map(lambda x: x[:-1], list(f)))
    f.close()
    
    check = False #Если записи нет, он записывает в конец файла
    
    f = open('data/members.csv', 'w')
    for person_info in members_array:
        person_array = person_info.split(',')
        if person_array[0] == str(person_id):
            if len(person_array) == 6: #Если человек хочет изменить про себя инфу
                person_info = str(person_id) + ',' + message
            else: #Обычное добавление
                person_info = person_info + ',' + message
            check = True
        f.write(person_info + '\n')
    if not check:
        f.write(str(person_id) + ',' + message + '\n')
    f.close()

def check_reg_status(): #Проверяет статус регистрации (возвращает True или False)
    f = open('data/admin.csv')
    admin_status = f.read().split(',')[1]
    f.close()
    return admin_status

def change_registration(): #Изменение статуса регистрации Если сейчас False, изменяет на True в бд
    f = open('data/admin.csv')
    admin_array = f.read().split(',')
    f.close()
    
    if admin_array[1] == 'False':
        admin_array[1] = 'True'
    else:
        admin_array[1] = 'False'
    
    f = open('data/admin.csv', 'w')
    f.write(','.join(admin_array))
    f.close()
    
def person_info(person_id): #Информация о персоне (выдает строку со всей информицией)
    person = 'ERROR'
    with open('data/members.csv') as file:
        for string in file:
            person_array = string[:-1].split(',')
            if str(person_id) == person_array[0]:
                person = 'Имя: ' + person_array[1] + '\n' + 'Фамилия: ' + person_array[2] + '\n' + 'UserName: ' + person_array[3] + '\n' + 'Где работает: ' + person_array[4] + '\n' + 'Хобби: ' + person_array[5] 
                break
    return person
