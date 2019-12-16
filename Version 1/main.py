#main.py

import telebot
from telebot import types

from classes import *
from database import *
from keyboard import *

token = ''

bot = telebot.TeleBot(f'{token}')

@bot.message_handler(content_types=['text'])
def start(message):
    status = check_status(message.from_user.id) #admin or noname or person
    if status == 'admin':
        admin(message)
    elif status == 'noname':
        noname(message)
    elif status == 'person':
        person(message)
    else:
        print(f'ERROR in start()\nId person: {id_man}')

        
#Если пользователь зашел в бот впервые
def noname(message):
    if message.text == 'Зарегистрироваться':
        registration_1(message)
    elif message.text == 'Узнать больше':
        bot.send_message(message.from_user.id, text=information_RC, reply_markup=key_noname)
    else:
        #Первое, что видит ноунейм
        bot.send_message(message.from_user.id, text='Добро пожаловать в Random Coffee. Ты еще не зарегистрировался. Что хочешь сделать?', reply_markup=key_noname)

#Если пользователь уже зареган
def person(message):
    pass

#Если это администратор
def admin(message):
    pass



#Регистрирует пользователя
#Спрашивает об изменении публичного имени и фимилии
def registration_1(message):
    id_person = message.from_user.id
    #Берем из открытого доступа инфу
    try:
        name_person = message.from_user.first_name
    except:
        name_person = None

    try:
        surname_person = message.from_user.last_name
    except:
        surname_person = None
            
    bot.send_message(id_person, text=f'Твое имя: {name_person}\nТвоя фамилия: {surname_person}\nВыбери что хочешь изменить', reply_markup=key_change_data)
    bot.register_next_step_handler(message, registration_2)

#Заносит в базу имя и фамилию
def registration_2(message):
    id_person = message.from_user.id
    #Находим имя и фамилию
    try:
        name_person = message.from_user.first_name
    except:
        name_person = None

    try:
        surname_person = message.from_user.last_name
    except:
        surname_person = None
        
    if message.text == 'Сохранить так':
        add_info(id_person, 'name', name_person)
        add_info(id_person, 'surname', surname_person)
        registration_3(message)
    
    elif message.text == 'Изменить имя':
        add_info(id_person, 'surname', surname_person)
        bot.send_message(message.from_user.id, text='Напиши свое имя')
        bot.register_next_step_handler(message, add_name)
    
    elif message.text == 'Изменить фамилию':
        add_info(id_person, 'name', name_person)
        bot.send_message(message.from_user.id, text='Напиши свою фамилию')
        bot.register_next_step_handler(message, add_surname)
    
    elif message.text == 'Изменить все':
        bot.send_message(message.from_user.id, text='Напиши свое имя и фамилию\nПример: Кирилл Сысоев')
        bot.register_next_step_handler(message, add_name_and_surname)
    
#Добавляет имя
def add_name(message):
    id_person = message.from_user.id
    name = message.text
    add_info(id_person, 'name', name)
    bot.send_message(message.from_user.id, text=f'Записанное имя: {name}. Правильно?', reply_markup=key_registration_name)
    bot.register_next_step_handler(message, registration_3)
    
#Добавляет фамилию
def add_surname(message):
    id_person = message.from_user.id
    surname = message.text
    add_info(id_person, 'surname', surname)
    bot.send_message(message.from_user.id, text=f'Записанная фамилия: {surname}. Правильно?', reply_markup=key_registration_surname)
    bot.register_next_step_handler(message, registration_3)

#Добавляет имя и фамилию одновременно
def add_name_and_surname(message):
    array = message.text.split()
    if len(array) == 2:
        id_person = message.from_user.id
        name = array[0]
        add_info(id_person, 'name', name)
        surname = array[1]
        add_info(id_person, 'surname', surname)
        bot.send_message(message.from_user.id, text=f'Записанное имя - {name}, фамилия - {surname}. Правильно?', reply_markup=key_registration)
        bot.register_next_step_handler(message, registration_3)
    else:
        bot.send_message(message.from_user.id, text='Ты ввел информацию не правильно. Давай попробуем еще раз. Напиши имя и фамилию.\nПример: Кирилл Сысоев')
        bot.register_next_step_handler(message, add_name_and_surname)

#Заносим в базу username
def registration_3(message):
    id_person = message.from_user.id
    if message.text == 'Изменить имя':
        bot.send_message(message.from_user.id, text='Введи имя еще раз')
        bot.register_next_step_handler(message, add_name)
    
    elif message.text == 'Изменить фамилию':
        bot.send_message(message.from_user.id, text='Введи фамилию еще раз')
        bot.register_next_step_handler(message, add_surname)
        
    elif message.text == 'Нет, изменить':
        bot.send_message(message.from_user.id, text='Введи имя и фамилию еще раз\nПример: Кирилл Сысоев')
        bot.register_next_step_handler(message, add_name_and_surname)
    else:
        username = message.from_user.username
        if username == None:
            bot.send_message(message.from_user.id, text='У тебя нет ника в telegram. Для того, чтобы с тобой могли связаться человек/ребята из общей группы, напиши свой номер телефона')
            bot.register_next_step_handler(message, add_username)
        else:
            add_info(id_person, 'username', '@'+username)
            registration_4(message)

#Добавляет телефон заместо username
def add_username(message):
    id_person = message.from_user.id
    telephone = message.text
    add_info(id_person, 'username', telephone)
    bot.send_message(message.from_user.id, text=f'Введенный телефон: {telephone}. Верно?', reply_markup=key_registration)
    bot.register_next_step_handler(message, registration_4)
        
#Заносим в базу хобби
def registration_4(message):
    if message.text == 'Нет, изменить':
        bot.send_message(message.from_user.id, text='Напишите свой телефон еще раз')
        bot.register_next_step_handler(message, add_username)
    else:
        bot.send_message(message.from_user.id, text='Опиши, чем увлекаешься')
        bot.register_next_step_handler(message, add_hobby)
        
#Добавляет хобби
def add_hobby(message):
    id_person = message.from_user.id
    hobby = message.text
    add_info(id_person, 'hobby', hobby)
    bot.send_message(message.from_user.id, text='Ввел без ошибок?', reply_markup=key_registration)
    bot.register_next_step_handler(message, registration_5)

#Заносим в базу работу
def registration_5(message):
    if message.text == 'Да':
        bot.send_message(message.from_user.id, text='Расскажи, где ты работаешь/работал')
        bot.register_next_step_handler(message, add_job)
    else:
        bot.send_message(message.from_user.id, text='Напиши свои увлечения еще раз (не забудь проверить перед отправкой)')
        bot.register_next_step_handler(message, add_hobby)
        
#Добавляет работу
def add_job(message):
    id_person = message.from_user.id
    job = message.text
    add_info(id_person, 'job', job)
    bot.send_message(message.from_user.id, text='Тут тоже не ошибся?', reply_markup=key_registration)
    bot.register_next_step_handler(message, registration_6)

#Последняя проверка
def registration_6(message):
    if message.text == 'Да':
        id_person = message.from_user.id
        info = get_info(id_person, 'all')
        name = info['name']
        surname = info['surname']
        username = info['username']
        hobby = info['hobby']
        job = info['job']
        bot.send_message(message.from_user.id, text=f'Перепроверь информацию\nИмя - {name}\nФамилия - {surname}\nUserName - {username}\nТвои увлечения - {hobby}\nТвоя профессиональная деятельность - {job}\nСохраняем ее?', reply_markup=key_registration_end)
        bot.register_next_step_handler(message, registration_7)
    else:
        bot.send_message(message.from_user.id, text='Напиши про свои профессиональные увлечения еще раз (не забудь проверить перед отправкой)')
        bot.register_next_step_handler(message, add_job)

#Конец регистрации
def registration_7(message):
    if message.text == 'Изменить имя':
        bot.send_message(message.from_user.id, text='Введи новое имя')
        bot.register_next_step_handler(message, edit_name)
    elif message.text == 'Изменить фамилию':
        bot.send_message(message.from_user.id, text='Введи новую фамилию')
        bot.register_next_step_handler(message, edit_surname)
    elif message.text == 'Изменить инфу о работе':
        bot.send_message(message.from_user.id, text='Расскажи о своих профессиональных интересах')
        bot.register_next_step_handler(message, edit_job)
    elif message.text == 'Изменить инфу о хобби':
        bot.send_message(message.from_user.id, text='Расскажи, чем ты интересуешься в жизни')
        bot.register_next_step_handler(message, edit_hobby)
    elif message.text == 'Изменить все':
        registration_1(message)
    else:
        id_person = message.from_user.id
        name = get_info(id_person, 'name')
        bot.send_message(message.from_user.id, text=f'Поздравляю, {name}! Твоя информация была успешна сохранена)', reply_markup=key_compliment) 

#Изменяет имя
def edit_name(message):
    add_info(message.from_user.id, 'name', message.text)
    message.text = 'Да'
    registration_6(message)

#Изменяет фамилию
def edit_surname(message):
    add_info(message.from_user.id, 'surname', message.text)
    message.text = 'Да'
    registration_6(message)

#Изменяет инфу о работе
def edit_job(message):
    add_info(message.from_user.id, 'job', message.text)
    message.text = 'Да'
    registration_6(message)

#Изменяет инфу о хобби
def edit_hobby(message):
    add_info(message.from_user.id, 'hobby', message.text)
    message.text = 'Да'
    registration_6(message)

    
    
    
bot.polling(none_stop=True, interval=0)