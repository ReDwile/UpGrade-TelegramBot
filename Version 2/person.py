from keyboard import *
from bot import *
from database import *

from noname import registration_7

# Если пользователь уже зареган
def person(message):
    if message.text == 'Посмотреть сохраненные данные':
        data = get_info(message.from_user.id, 'all')
        name = data['name']
        surname = data['surname']
        username = data['username']
        hobby = data['hobby']
        job = data['job']
        bot.send_message(message.from_user.id,
                         text=f'Данные, которые сохранены в бд:\nИмя: {name}\nФамилия: {surname}\nUserName: {username}\nИнтересы: {hobby}\nПрофессиональные интересы: {job}',
                         reply_markup=key_person)

    elif message.text == 'Изменить данные':
        bot.send_message(message.from_user.id, text='Что именно хочешь изменить?', reply_markup=key_select_changes)
        bot.register_next_step_handler(message, registration_7)

    elif message.text == 'Удалить мои данные':
        # Удаляет все данные пользователя по id
        delete_data(message.from_user.id)
        bot.send_message(message.from_user.id, text='Ваши данные успешно удалены\n/start')

    elif message.text == 'Оставить отзыв о работе':
        bot.send_message(message.from_user.id, text='Опиши свое взаимодействие с RandomCoffee')
        bot.register_next_step_handler(message, feedback_start)

    else:
        bot.send_message(message.from_user.id, text='Выбери, что хочешь сделать', reply_markup=key_person)

# Сохраняет отзыв
def feedback_start(message):
    try:
        feedback(message.from_user.id, message.text)
    except:
        logi('Ошибка в person feedback_start() ID: ' + str(message.from_user.id) + ' text: ' + str(message.text))

    bot.send_message(message.from_user.id, text='Информация была отправлена администраторам. Мы постараемся сделать сервис лучше))\nСпасибо за старания!', reply_markup=key_person)