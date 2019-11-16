import telebot

from algorithms import *
from read_database import *

from token_public import *
#from token_private import *

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
    if message.text == '/change': #Изменяет статус регистрации
        change_registration()
        if check_reg_status() == 'True':
            for person_id in persons():
                bot.send_message(int(person_id), text='Открыта регистрация на новую неделю Random Coffee. Ты автоматически находишься в списках зарегистрированных.\n/remove - если не хочешь участвовать на этой неделе\n/about - если хочешь посмотреть, какая сейчас информация находится о тебе\n/replacement - если хочешь изменить информацию')
        message.text = '/info'
        admin(message)
    elif message.text == '/send': #Отсылает сообщение всем зареганным людям
        bot.send_message(message.from_user.id, text='Напиши сообщение, которое будет разосланно всем зарегистрированным участникам:')
        bot.register_next_step_handler(message, sendmessage)
    elif message.text == '/begin': #Запускает алгоритм распределения по командам
        array_error = error_len() #Возвращает [('name1', 'surname1', 'id'),(),()] - людей, у которых ошибка в веденных дынных
        if len(array_error) == 0:
            begin_algo_2(message)
        else:
            string = 'Ошибка\n'
            for name, surname, person_id in array_error:
                string = string + name + ' ' + surname + '\n'
            bot.send_message(message.from_user.id, text=string + 'У этих людей либо не до конца записана инфа в Базе Данных. Нельзя включить алгоритм из-за этих людей.\n/continue - запустить алгоритм распределения (информация об этих людях будет удалена из Базы Данных и они не будут принимать участие в Random Coffee на этой неделе')
            bot.register_next_step_handler(message, check_error)
        message.text = '/info'
        admin(message)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, text='Ты находишься в режиме администратора. Если статус записи на Random Coffee: False - регистрация закрыта, если True - регистрация открыта. Перед тем, как запускать алгоритм распределения зарегистрированных участников по группам, статус регистрации должен быть False.')

        message.text = '/info'
        admin(message)
    else:
        bot.send_message(message.from_user.id, text=f'Текущий статус записи на рандом-кофе: {check_reg_status()}\nКоличество зарегистрированных участников: {len(persons())}')
        bot.send_message(message.from_user.id, text='/change - изменяет статус регистрации\n/begin - запуск алгоритма распределения по командам\n/help - информация, объясняющая, как работать с ботом\n/send - написать всем зарегистрированным участникам\n/info - актуальная информация по активности')

def interaction(message):
    if message.text == '/registration':
        if check_reg_status() == 'True':
            bot.send_message(message.from_user.id, text='Напиши свое имя')
            bot.register_next_step_handler(message, firstname)
        else:
            bot.send_message(message.from_user.id, text='Регистрация пока закрыта')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, этот бот регистрирует тебя на Random Coffee.\nСначала напиши /registration для начала регистрации. Бот начнет спрашивать тебя о необходимой информации. В дальнейшем она будет отправлена твоему партнеру по Random Coffee. Ну что, начнем?')
    else:
        bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, это основные команды:\n/registration - регистрация на Random Coffee\n/help - подробная информация')


def replacement(message):
    if message.text == '/replacement':
        remove_person(message.from_user.id)
        message.text = '/registration'
        interaction(message)
    elif message.text == '/remove':
        remove_person(message.from_user.id)
        if chek_admin(message.from_user.id) != 'member':
            bot.send_message(message.from_user.id, text='Информация о тебе удалена. Если все же захочешь участвовать в Random Coffee на это недели, напиши /registration')
    else:
        try:
            bot.send_message(message.from_user.id, text=f'Ты зарегистрирован на Random Coffee этой недели\nТекущая сохраненная информация о тебе:\n{person_info(message.from_user.id)}\n/replacement - если хочешь обновить информацио о себе\n/remove - если не хочешь участвовать на этой недели в Random Coffee')
        except:
            bot.send_message(message.from_user.id, text='Ошибка записи в Базу Данных. Напиши @redwile об ошибке и пройди заного регистрацию, написав /replacement')

def firstname(message):
    name = message.text
    insert_register(name, message.from_user.id)
    bot.send_message(message.from_user.id, text='Теперь напиши фамилию')
    bot.register_next_step_handler(message, lastname)

def lastname(message):
    surname = message.text
    insert_register(surname, message.from_user.id)
    if message.from_user.username == None:
        insert_register(f'Нет никнейма', message.from_user.id)
        bot.send_message(message.from_user.id, text='Расскажи, где ты работаешь')
        bot.register_next_step_handler(message, job)
    else:
        insert_register(f'@{message.from_user.username}', message.from_user.id)
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
    bot.send_message(message.from_user.id, text=f'Сохраненная информация:\n{person_info(message.from_user.id)}')
    bot.send_message(message.from_user.id, text='Спасибо за регистрацию\nЭта информация будет отправлена твоему будущему партнеру по Random coffee\nЖди даты окончания регистрации, тебе придет сообщение с информацией твоего парнера))')
    bot.send_message(message.from_user.id, text='/replacement - если хочешь изменить информацио о себе')

def send_person_message(array): #Рассылает участникам сообщения о парах (в массиве есть массив из id участников, находящихся в одной группе)
    for group in array:
        for person_id in group:
            bot.send_message(int(person_id), text='Следующую неделю, в рамках Random coffee, ты проведешь с:')
            for i in range(len(group)):
                if person_id != group[i]:
                    bot.send_message(int(person_id), text=person_info(group[i]))
            bot.send_message(int(person_id), text='Быстрее пиши в личку и договаривайтесь на встречу!!! :)')

def sendmessage(message): #Рассылает сообщение всем участникам
    persons_array = persons()
    for person_id in persons_array:
        bot.send_message(int(person_id), text=message.text)
    bot.send_message(message.from_user.id, text=f'Сообщение было разослано {len(persons_array)} зарегистрированным участникам')
    message.text = '/info'
    admin(message)

def begin_algo_2(message):
        if check_reg_status() == 'True':
            bot.send_message(message.from_user.id, text='Для начала останови регистрацию, написав /change')
        else:
            check_send = begin_algo()
            #print(check_send) #Пишет в командную строку группу и участников в них
            send_person_message(check_send) #Рассылает информацию участникам, находящимся в общих группах
            bot.send_message(message.from_user.id, text='Участники распределены. Им разосланы сообщения об их парах')

def check_error(message):
    if message.text == '/continue':
        if check_reg_status() == 'True':
            change_registration()
        array_error = error_len() #Возвращает [('name1', 'surname1', 'id'),(),()] - людей, у которых ошибка в веденных дынных
        for name, surname, id_person in array_error:
            remove_person(int(id_person))
        begin_algo(message)
    else:
        admin(message)

bot.polling(none_stop=True, interval=0)
