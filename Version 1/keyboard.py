#keyboard.py

import telebot
from telebot import types

information_RC = 'Бот регистрирует тебя на Random Coffee. Помимо тебя здесь регистрируются другие люди. Потом алгоритм разбивает вас на группы по интересам. Вам дается неделя для общей встречи (например, в кафе, за чашечкой кофе). Распределение на команды происходит каждую неделю. Удачи)'

key_noname = telebot.types.ReplyKeyboardMarkup(True)
key_noname.row('Узнать больше')
key_noname.row('Зарегистрироваться')

key_change_data = telebot.types.ReplyKeyboardMarkup(True)
key_change_data.row('Сохранить так')
key_change_data.row('Изменить имя')
key_change_data.row('Изменить фамилию')
key_change_data.row('Изменить все')

key_registration_name = telebot.types.ReplyKeyboardMarkup(True)
key_registration_name.row('Да')
key_registration_name.row('Изменить имя')

key_registration_surname = telebot.types.ReplyKeyboardMarkup(True)
key_registration_surname.row('Да')
key_registration_surname.row('Изменить фамилию')

key_registration = telebot.types.ReplyKeyboardMarkup(True)
key_registration.row('Да')
key_registration.row('Нет, изменить')

key_registration_end = telebot.types.ReplyKeyboardMarkup(True)
key_registration_end.row('Да, все супер')
key_registration_end.row('Изменить имя')
key_registration_end.row('Изменить фамилию')
key_registration_end.row('Изменить инфу о работе')
key_registration_end.row('Изменить инфу о хобби')
key_registration_end.row('Изменить все')

key_compliment = telebot.types.ReplyKeyboardMarkup()
key_compliment.row('Принять поздравления!')