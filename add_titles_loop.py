# Просим ввести основной заголовок
title = []

while True: # задаем цикл
    add_title = input('Можете ввести заголовок или оставьте поле пустым ') # Просим ползователя ввести данные
    if add_title == '' or add_title == ' ':# Проверяем данные пользователя где пустое значение остановит цикл
        break
    elif title.count(add_title): # проверка на уникальность данных
            print('Такой заголовок уже есть', add_title)
            add_title = input('Введите другой заголовок') # Заменяем повторившееся значение
            title.append(add_title)  # Добавление значения в список через метод .append
    else:
        title.append(add_title)  # Добавление значения в список через метод .append

print(title) # Вывод всего списка