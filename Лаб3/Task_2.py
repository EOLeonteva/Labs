# TODO Напишите функцию find_common_participants

def find_common_participants (participants_first_group, participants_second_group, separator=','):
    group1 = participants_first_group.split(separator)
    group2 = participants_second_group.split(separator)

    common_participants = list(set(group1).intersection(group2))
    common_participants.sort()

    return common_participants

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common)
