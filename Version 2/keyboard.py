import telebot
from telebot import types

information_RC = 'Бот регистрирует тебя на Random Coffee. Помимо тебя здесь регистрируются другие люди. Потом алгоритм разбивает вас на группы по интересам. Вам дается неделя для общей встречи (например, в кафе, за чашечкой кофе). Распределение на команды происходит каждую неделю. Удачи)'
help_message = 'Ты в режиме администратора. Ты можешь написать сообщение всем зарегистрированным участникам. Так же запустить алгоритм распределение участников по группам (на основе их интересов)'
info_person = 'Полностью зарегистрировались следующие люди:\n{0}\nЧастично, следующие:\n{1}Участвовать могут только полностью зарегистрированные люди. Что делать?'

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

key_person = telebot.types.ReplyKeyboardMarkup(True)
key_person.row('Посмотреть сохраненные данные')
key_person.row('Изменить данные')
key_person.row('Удалить мои данные')
key_person.row('Оставить отзыв о работе')

key_select_changes = telebot.types.ReplyKeyboardMarkup(True)
key_select_changes.row('Посмотреть данные')
key_select_changes.row("Изменить имя")
key_select_changes.row('Изменить фамилию')
key_select_changes.row('Изменить инфу о хобби')
key_select_changes.row('Изменить инфу о работе')
key_select_changes.row('Изменить все')
key_select_changes.row('Назад')

key_message_admin = telebot.types.ReplyKeyboardMarkup(True)
key_message_admin.row('Хорошо')

key_person_reg_info = telebot.types.ReplyKeyboardMarkup(True)
key_person_reg_info.row('Запустить алгоритм')
key_person_reg_info.row('Написать незареганным людям')
key_person_reg_info.row('Назад')

key_admin_panel = telebot.types.ReplyKeyboardMarkup(True)
key_admin_panel.row('Актуальная инфа о регистрации')
key_admin_panel.row('Написать участникам')
key_admin_panel.row('Запустить алгоритм')
key_admin_panel.row('Help')

key_person_reg_now = telebot.types.ReplyKeyboardMarkup(True)
key_person_reg_now.row('Актуальная инфа о регистрации')
key_person_reg_now.row('Запустить алгоритм')
key_person_reg_now.row('Назад')
