import telebot

from admin import *
from noname import *
from person import *
from bot import *

@bot.message_handler(content_types=['text'])
def start(message):
    status = check_status(message.from_user)  # admin or noname or person

    if status == 'admin':
        admin(message)

    elif status == 'noname':
        noname(message)

    elif status == 'person':
        person(message)

    else:
        print(f'ERROR in start()')



# Работает с эксель-файлом на компе
def check_status(id_person):
    '''Получает id пользователя, выводит статус (admin, noname, person, adminandperson)'''
    filename_name = 'data/persons_data_' + str(v_file()) + '.xlsx'
    wb = openpyxl.load_workbook(filename=filename_name)
    sheet = wb['admin']
    # username администраторов записаны в строчку
    id_person_admin = id_person.username
    for i in range(1, sheet.max_column + 1):
        id_person_db = sheet.cell(row=1, column=i).value
        # Временное решение, тк очень часто вылетает бот именно здесь
        try:
            if id_person_db != None and id_person_admin != None and id_person_db.lower() == id_person_admin.lower():
                return 'admin'
        except:
            logi('Ошибка в main check_status() строчка 40: id_person_db ' + str(id_person_db) + ' , id_person_admin ' + str(id_person_admin))
            return 'admin'

    id_person = id_person.id
    sheet = wb['person']
    for i in range(2, sheet.max_row + 1):
        id_person_db = sheet.cell(row=i, column=1).value
        if id_person_db == id_person:
            return 'person'
    return 'noname'


bot.polling(none_stop=True, interval=0)