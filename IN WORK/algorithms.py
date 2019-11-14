import random

def begin_algo(): #Распределяет зарегистрированных участников на группы, выдает массив массивов id участников
    member_array = []
    with open('data/members.csv') as file:
        for i in file:
            member_array.append(i.split(',')[0])
    
    random.shuffle(members_array)
    
    kol = len(members_array)//2
    members = [[] for i in range(kol)]
    
    for i in range(len(members_array)):
        members[i%kol].append(member_array[i])
    return members

def send_person_message(array): #Рассылает участникам сообщения о парах
    for group in array:
        i = len(group)-1
        for person_id in group:
            for i in range(len(group)):
                if person_id != group[i]:
                    bot.send_message(person_id, text=person_info(group[i]))
