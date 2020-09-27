from keyboard import *
from bot import *
from database import *
from algorithms import *

# Если это администратор
def admin(message):
    if message.text == 'Написать участникам':
        bot.send_message(message.from_user.id, text='Напиши сообщение, которое отправится всем участникам')
        array_id = saved_id()
        bot.register_next_step_handler(message, message_nreg, array_id)

    elif message.text == 'Актуальная инфа о регистрации':
        data_all, data_nall = user_dicts()
        person_r = ''
        person_nr = ''
        for i in data_all.keys():
            person = data_all[i]
            person_r += person['name'] + ' ' + person['surname'] + '\n'
        person_r += f'Всего: {len(data_all)}\n'

        for i in data_nall.keys():
            person = data_nall[i]
            person_nr += person['name'] + ' ' + person['surname'] + '\n'
        person_nr += f'Всего: {len(data_nall)}\n'
        bot.send_message(message.from_user.id, text=info_person.format(person_r, person_nr), reply_markup=key_person_reg_info)

    elif message.text == 'Запустить алгоритм':
        data_all, data_nall = user_dicts()

        # Записываем логи
        logi('Зареганные люди: ' + str(data_all))
        logi('Незареганные люди: ' + str(data_nall))

        # data_all = {id1: {'name': 'Kirill', 'surname': ...}, ...}
        # data = [[id1, id2], [id3, id4], [id5, id6, id7]]
        data = algo(data_all)

        # Записываем логи
        logi('Распределение по группам: ' + str(data))
        logi('Количество групп: ' + str(len(data)))
        logi('Уведомленные люди: ')

        save_new_info(data)

        if len(data) != 0:
            for group in data:
                # Оповещает людей о предстоящей рассылки
                for person in group:
                    try:
                        bot.send_message(person['id'], text='Следующую неделю ты проведешь в компании...')

                        # Записываем логи
                        logi(str(person))
                    except:
                        # Записываем проблемные логи
                        logi('Те, у кого возникли проблемы!!!: ' + str(person))
                        delete_data(person['id'])

                mailing_message_group(group)

                # Послесловие
                for person in group:
                    bot.send_message(person['id'], text='Пришло время поделиться радостной новостью\nБыстрее пиши в лс, и договаривайтесь о встрече))\n(Не забудь оставить отзыв)')

            bot.send_message(message.from_user.id, text='Ребята были распределены по группам. Им разослали сообщения')
            print('Распределение прошло успешно')
            print()
        else:
            bot.send_message(message.from_user.id, text='Произошла ошибка в файле algorithms')

    elif message.text == 'Help':
        bot.send_message(message.from_user.id, text=help_message)

    elif message.text == 'Написать незареганным людям':
        data_all, data_nall = user_dicts()
        bot.send_message(message.from_user.id, text='Напишите, что хотите разослать частично зареганным людям')
        bot.register_next_step_handler(message, message_nreg, data_nall)

    else:
        bot.send_message(message.from_user.id, text='Привет. Ты в режиме администратора. \nВот твой функционал:', reply_markup=key_admin_panel)


# Берет текст, который пишет администратор для отправки незареганным людям
def message_nreg(message, data_nall):
    text_person = message.text
    bot.send_message(message.from_user.id, text=f'Отправить следующий текст?\n{text_person}', reply_markup=key_registration)
    bot.register_next_step_handler(message, message_nreg1, text_person, data_nall)

# Спрашивает перед отправкой, изменить или нет сообщение
def message_nreg1(message, text_person, data_nall):
    if message.text == 'Да':
        if type(data_nall) == dict:
            for person_id in data_nall.keys():
                try:
                    bot.send_message(person_id, text=text_person + '\nС уважением, администратор')
                except:
                    # Записываем проблемные логи
                    person_information = get_info(person_id, 'all')
                    logi('Те, у кого возникли проблемы при отправки сообщения!!! (id): ' + str(person_information))
                    delete_data(person_id)

            bot.send_message(message.from_user.id, text='Сообщение было разослано\nТеперь что сделать?', reply_markup=key_person_reg_now)

        elif type(data_nall) == list:
            for person_id in data_nall:
                try:
                    bot.send_message(person_id, text=text_person + '\nС уважением, администратор')
                except:
                    # Записываем проблемные логи
                    person_information = get_info(person_id, 'all')
                    logi('Те, у кого возникли проблемы при отправки сообщения!!! (id): ' + str(person_information))
                    delete_data(person_id)

            bot.send_message(message.from_user.id, text='Сообщение было разослано', reply_markup=key_message_admin)

        else:
            print('Ошибка в файле admin, в функции message_nreg1')

    else:
        bot.send_message(message.from_user.id, text='Напишите еще раз текст')
        bot.register_next_step_handler(message, message_nreg, data_nall)


# Рассылает сообщение в группы
def mailing_message_group(group):
    if len(group) > 1:
        for i in range(1, len(group)):
            person_1 = group[0]
            person_2 = group[i]

            # Второй пользователь получает информацию о первом
            bot.send_message(person_2['id'], text='{0} {1}\nusername: {2}\nРабота - {3}\nИнтересы - {4}'.format(person_1['name'], person_1['surname'], person_1['username'], person_1['job'], person_1['hobby']))

            # Первый пользователь получает информацию о втором
            bot.send_message(person_1['id'], text='{0} {1}\nusername: {2}\nРабота - {3}\nИнтересы - {4}'.format(person_2['name'], person_2['surname'], person_2['username'], person_2['job'], person_2['hobby']))

        mailing_message_group(group[1:])

