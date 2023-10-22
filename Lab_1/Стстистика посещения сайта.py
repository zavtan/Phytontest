users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
users_ = {'Общее количество': 0, 'Уникальные посещения': 0}
users_num = len(users)
users_count = len(set(users))
users_['Общее количество'] = users_num
users_['Уникальные посещения'] = users_count
print(users_)

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
