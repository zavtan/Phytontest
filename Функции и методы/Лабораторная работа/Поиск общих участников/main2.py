# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, separator=','):

    participants_first_group = str1.split(separator)
    participants_second_group = str2.split(separator)

    common_participants = list(set(participants_first_group) & set(participants_second_group))
    common_participants.sort()

    return common_participants


str1 = "Иванов|Петров|Сидоров"
str2 = "Петров|Сидоров|Смирнов"

find_common_participants(str1, str2)




# TODO Провеьте работу функции с разделителем отличным от запятой



