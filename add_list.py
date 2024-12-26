# создание заметок
print('Добавтье до 3-ех ключевых слов(ничего не вводите для пропуска)')

num = 0
key_list = []

while num < 3:
    key_title1 = input(f'Основные темы')
    if key_title1 == '' or key_title1 ==' ':
        num += 1
        key_title3 = None
    else:
        num += 1
        key_list.append(key_title1)
    key_title2 = input(f'Персонажи')
    if key_title2 == '' or key_title1 ==' ':
        num += 1
        key_title3 = None
    else:
        num += 1
        key_list.append(key_title2)
    key_title3 = input(f'Рекомендации для чтения')
    if key_title3 == '' or key_title1 ==' ':
        num += 1
        key_title3 = None
    else:
        num += 1
        key_list.append(key_title3)
        print('Добавлено максимальное количество ключевых слов')
        print('Это ваши заголовки:')

print('Основные темы:',key_title1)
print('Персонажи:',key_title2)
print('Рекомендации для чтения:',key_title3)