import random

def begin_algo(): #Распределяет зарегистрированных участников на группы, выдает массив массивов id участников
    members_array = []
    with open('data/members.txt') as file:
        for i in file:
            members_array.append(i.split('><')[0])
    if len(members_array) <= 3:
        members = [members_array]
    else:
        random.shuffle(members_array)

        kol = len(members_array)//2
        members = [[] for i in range(kol)]

        for i in range(len(members_array)):
            members[i%kol].append(members_array[i])
    return members