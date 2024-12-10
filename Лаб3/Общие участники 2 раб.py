def find_common_participants(list_1, list_2, period = ','):

    list_1 = list_1.split(period)

    list_2 = list_2.split(period)

    common_participants = list(set(list_1).intersection(list_2))

    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"

participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, period = '|')

print(result)