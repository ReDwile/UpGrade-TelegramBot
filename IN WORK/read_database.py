def chek_admin(person_id): #Проверяет, является ли человек админом или нет (admin, member or none)
    person = 'none'

    f = open('data/admin.txt')
    admin_id = f.read().split('><')[0]
    f.close()

    with open('data/members.txt') as file:
        for person_str in file:
            person_array = person_str.split('><')
            if person_array[0] == str(person_id):
                person = 'member'

    if str(person_id) == admin_id:
        person = 'admin'

    return person

def insert_register(message, person_id): #записывает в бд имя(инфу) по id
    f = open('data/members.txt')
    members_array = list(map(lambda x: x[:-1], list(f)))
    f.close()

    check = False #Если записи нет, он записывает в конец файла

    f = open('data/members.txt', 'w')
    for person_info in members_array:
        person_array = person_info.split('><')
        if person_array[0] == str(person_id):
            person_info = person_info + '><' + message
            check = True
        f.write(person_info + '\n')
    if not check:
        f.write(str(person_id) + '><' + message + '\n')
    f.close()

def check_reg_status(): #Проверяет статус регистрации (возвращает True или False)
    f = open('data/admin.txt')
    admin_status = f.read().split('><')[1]
    f.close()
    return admin_status

def change_registration(): #Изменение статуса регистрации Если сейчас False, изменяет на True в бд
    f = open('data/admin.txt')
    admin_array = f.read().split('><')
    f.close()

    if admin_array[1] == 'False':
        admin_array[1] = 'True'
    else:
        admin_array[1] = 'False'

    f = open('data/admin.txt', 'w')
    f.write('><'.join(admin_array))
    f.close()

def person_info(person_id): #Информация о персоне (выдает строку со всей информицией)
    person = 'ERROR'
    with open('data/members.txt') as file:
        for string in file:
            person_array = string[:-1].split('><')
            if str(person_id) == person_array[0]:
                person = 'Имя: ' + person_array[1] + '\n' + 'Фамилия: ' + person_array[2] + '\n' + 'UserName: ' + person_array[3] + '\n' + 'Где работает: ' + person_array[4] + '\n' + 'Хобби: ' + person_array[5]
                break
    return person

def remove_person(person_id): #Удаляет зарегистрированного человека из бд
    f = open('data/members.txt')
    members_array = list(map(lambda x: x[:-1], list(f)))
    f.close()

    f = open('data/members.txt', 'w')
    for person_info in members_array:
        person_array = person_info.split('><')
        if person_array[0] != str(person_id):
            f.write(person_info + '\n')
    f.close()

def persons(): #Выводит массив с зарегистрированными участниками
    persons = []
    with open('data/members.txt') as file:
        for person_str in file:
            persons.append(person_str.split('><')[0])
    return persons

def error_len(): #Возвращает [('name1', 'surname1', 'id'),(),()] - людей, у которых ошибка в веденных дынных
    persons = []
    with open('data/members.txt') as file:
        for person_str in file:
            array = person_str.split('><')
            if len(array) != 6:
                info_tuple = [array[1]]
                try:
                    info_tuple.append(array[2])
                except:
                    info_tuple.append('(Не успел написать фамилию)')
                info_tuple.append(int(array[0]))
                persons.append(info_tuple)
    return persons
