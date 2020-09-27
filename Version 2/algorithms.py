import random

def algo(data):
    # data = {id1: {'name': 'Name1', ...}, ...} - просто список полностью зареганных людей

    members_array = list(data.keys())
    if len(members_array) < 2:
        return []

    # for i in range(3):
    #     random.shuffle(members_array)

    k = len(members_array)
    kol = len(members_array) // 2
    data_group = []

    for i in range(kol):
        person_1 = data[members_array[i]]
        person_1['id'] = members_array[i]
        data_group.append(person_1)
        person_2 = data[members_array[k-i-1]]
        person_2['id'] = members_array[k-i-1]
        data_group.append(person_2)

    data_group_array = [[] for i in range(kol)]
    p = 0
    for i in range(0, len(data_group), 2):
        data_group_array[p].append(data_group[i])
        data_group_array[p].append(data_group[i+1])
        p += 1

    if k % 2 == 1:
        person = data[members_array[kol]]
        person['id'] = members_array[kol]
        data_group_array[-1].append(person)

    return data_group_array
