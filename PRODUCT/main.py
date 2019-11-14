import telebot

from algorithms import *
from read_database import *

token = ''
bot = telebot.TeleBot(f'{token}')

@bot.message_handler(content_types=['text'])
def main(message):
    man = chek_admin(message.from_user.id)
    if man == 'admin':
        admin(message)
    elif man == 'member':
        replacement(message)
    else:
        interaction(message)
    
def admin(message):
    if message.text == '/change':
        change_registration()
    if message.text == '/begin':
        if check_reg_status() == 'True':
            bot.send_message(message.from_user.id, text='Для начала останови регистрацию')
        else:
            check_send = begin_algo()
            send_person_message(check_send)
            if len(check_send)>2:
                bot.send_message(message.from_user.id, text='Участники распределены. Им разосланы сообщения об их парах')
            else:
                bot.send_message(message.from_user.id, text='Произошла ошибка. Напиши @redwile об этом.')
    bot.send_message(message.from_user.id, text=f'Текущий статус записи на рандом-кофе: {check_reg_status()}\nДля изменения статуса регистрации напиши /change\nДля активации алгоритма распределения участников по командам напиши /begin (Для работы алгоритма участников зареганых участников должно быть больше 3)')
    
def interaction(message):
    if message.text == '/start':
        if check_reg_status() == 'True':
            bot.send_message(message.from_user.id, text=f'Привет! Для начала необходимо зарегистрироваться\nНапиши свое имя')
            bot.register_next_step_handler(message, firstname)
        else:
            bot.send_message(message.from_user.id, text='Регистрация пока закрыта')
    else:
        bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, для начала работы напиши /start')

def replacement(message):
    bot.send_message(message.from_user.id, text='Ты уже зарегистрирован\nЕсли хочешь обновить информацио о себе, напиши /replacement')
    bot.register_next_step_handler(message, replacement_answer)

def firstname(message):
    name = message.text
    insert_register(name, message.from_user.id)
    bot.send_message(message.from_user.id, text='Теперь напиши фамилию')
    bot.register_next_step_handler(message, lastname)

def lastname(message):
    surname = message.text
    insert_register(surname, message.from_user.id)
    bot.send_message(message.from_user.id, text='Напиши свой ник в телеге (с @)')
    bot.register_next_step_handler(message, username)
    
def username(message):
    username = message.text
    insert_register(username, message.from_user.id)
    bot.send_message(message.from_user.id, text='Расскажи, где ты работаешь')
    bot.register_next_step_handler(message, job)
    
def job(message):
    job = message.text
    insert_register(job, message.from_user.id)
    bot.send_message(message.from_user.id, text='Опиши теперь чем ты увлекаешься (свои хобби)')
    bot.register_next_step_handler(message, hobby)
    
def hobby(message):
    hobby = message.text
    insert_register(hobby, message.from_user.id)
    bot.send_message(message.from_user.id, text=f'Спасибо за ответ\nЭта информация будет отправлена твоему партнеру по встрече\nЖди даты распределения))\nСохраненная информация:\n{person_info(message.from_user.id)}')

def replacement_answer(message):
    if message.text == '/replacement':
        message.text = '/start'
        interaction(message)
        
def send_person_message(array): #Рассылает участникам сообщения о парах (в массиве есть массив из id участников, находящихся в одной группе)
    for group in array:
        for person_id in group:
            for i in range(len(group)):
                if person_id != group[i]:
                    bot.send_message(person_id, text=person_info(group[i]))

bot.polling(none_stop=True, interval=0)
