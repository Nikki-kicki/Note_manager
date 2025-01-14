from datetime import datetime



print('Здравствуйте, это менеджер заметок на Python:)')
print('Приступим')

notes_list = []
note1 = {}

# удаление заметок
def delete_note():
    while True:
        print('Вы хотите создать/удалить заметку?(введите создать или удалить)\n')
        delete_note = str(input().lower())
        if delete_note == 'cjplfnm' or delete_note == 'создать':
            flags = False
        elif delete_note == 'elfkbnm' or delete_note == 'удалить':
            print(notes_list)
            print('Заметку с каким заголовком вы хотите удалить?')
            delete_from_titel = str(input())
            if notes_list.count(delete_from_titel):
                delete = str(input('Удалить?(да или нет)\n').lower())
                if delete == 'lf' or delete == 'да':
                    notes_list.remove(delete_from_titel)
                    break
                else:
                    break
            else:
                print('Совпадений не найдено:(')
                print('Ваши заголовки: ')
                print(notes_list)
                continue
    # создание имени пользователя
    user = input('Введите имя пользователя:\n')
    note1.update(username=user)
    print('Здравствуйте: ', note1['username'])

    # создание заголовков
    title = []
    while True:  # задаем цикл
        add_title = input(
            'Можете ввести несколько заголовков или оставьте поле пустым \n')  # Просим ползователя ввести данные
        if add_title == '' or add_title == ' ':  # Проверяем данные пользователя где пустое значение остановит цикл
            break
        elif title.count(add_title):  # проверка на уникальность данных
            print('Такой заголовок уже есть', add_title)
            add_title = input('Введите другой заголовок ')  # Заменяем повторившееся значение
            title.append(add_title)  # Добавление значения в список через метод .append
        else:
            title.append(add_title)  # Добавление значения в список через метод .append
    note1.update(titles=title)
    print('Ваши заголовки: ', note1['titles'])

    # создание заметок
    print('Добавтье до 3-ех ключевых слов(ничего не вводите для пропуска)')

    num = 0
    key_list = []

    while num < 3:
        key_title1 = input(f'Основные темы ')
        if key_title1 == '' or key_title1 == ' ':
            num += 1
            key_title1 = None
        else:
            num += 1
            key_list.append(key_title1)
        key_title2 = input(f'Персонажи ')
        if key_title2 == '' or key_title2 == ' ':
            num += 1
            key_title2 = None
        else:
            num += 1
            key_list.append(key_title2)
        key_title3 = input(f'Рекомендации для чтения ')
        if key_title3 == '' or key_title3 == ' ':
            num += 1
            key_title3 = None
        else:
            num += 1
            key_list.append(key_title3)
            print('Добавлено максимальное количество ключевых слов')
            print('Это ваши заголовки:')

    print('Основные темы:', key_title1)
    print('Персонажи:', key_title2)
    print('Рекомендации для чтения:', key_title3)
    note1.update(content=key_list)

    # создание статуса заметки
    status = None
    status_accept = None


    while True:  # цикл перезаписи значения для status
        try:
            print('Текущий статус заметки: В процессе')
            print('Для смены статуса нажмите одну из приведенных цифр\n'
                  '1 - Выполнено\n'
                  '2 - В процессе\n'
                  '3 - Отложено\n')
            status_changer = int(input())
            if status_changer == 1 and status_changer != '' or ' ':  # вариант для значения 1
                status = 'Выполнено'
                print('Статус изменен на: ', status)
                status_accept = str(input('Изменить статус заметки(да / нет)?\n').lower()) # уточнение для изменения статуса
                try:
                    if status_accept == 'нет' or status_accept == 'ytn':
                        print('Статус сохранен на: ', status)
                        break
                    if status_accept == 'да' or status_accept == 'lf':
                        print('Текущий статус заметки: ', status)
                        print('Для сменый статуса нажмите одну из приведенных цифр\n'
                            '1 - Выполнено\n'
                            '2 - В процессе\n'
                            '3 - Отложено\n')
                except:
                    print('Пожалуйста, введите да или нет')
            elif status_changer == 2 and status_changer != '' or ' ':  # вариант для значения 2
                status = 'В процессе'
                print('Статус изменен на: ', status)
                status_accept = str(input('Изменить статус заметки(да / нет)?\n').lower())
                try:
                    if status_accept == 'нет' or status_accept == 'ytn':
                        print('Статус сохранен на: ', status)
                        break
                    if status_accept == 'да' or status_accept == 'lf':
                        print('Текущий статус заметки: ', status)
                        print('Для сменый статуса нажмите одну из приведенных цифр\n'
                            '1 - Выполнено\n'
                            '2 - В процессе\n'
                            '3 - Отложено\n')
                except:
                    print('Пожалуйста, введите да или нет')
            elif status_changer == 3 and status_changer != '' or ' ':  # вариант для значения 3
                status = 'Отложено'
                print('Статус изменен на: ', status)
                status_accept = str(input('Изменить статус заметки(да / нет)?\n').lower())
                try:
                    if status_accept == 'нет' or status_accept == 'ytn':
                        print('Статус сохранен на: ', status)
                        break
                    if status_accept == 'да' or status_accept == 'lf':
                        print('Текущий статус заметки: ', status)
                        print('Для сменый статуса нажмите одну из приведенных цифр\n'
                            '1 - Выполнено\n'
                            '2 - В процессе\n'
                            '3 - Отложено\n')
                except:
                    print('Пожалуйста, введите да или нет')
            else:
                while status_changer < 1 or status_changer > 3:  # исключение ошибки
                    print('Убедитесь в правильности ввода')
                    break
        except:
            print('Пожалуйста повторите ввод используя цифры')
    note1.update(status=status)

    # создание даты начала заметки
    today = datetime.today()
    print('Cегодня')
    print(f'{today:%d-%m-%Y}', ' Пожалуйста, введите дату создания заметки')
    while True:
        try:
            created_date = input('Введите дату в таком формате: xx-xx-xxxx \n') # ввод даты пользователя  формате дд-мм-гггг
            created_date = datetime.strptime(created_date, '%d-%m-%Y')
            created_date = datetime.strftime(created_date, '%d-%m-%Y')
            break
        except:
            print('Введен неверный формат даты, попробуйте еще раз ')
    note1.update(created_date=created_date)
    print('Дата создания заметки: ', note1['created_date'])

    # создание даты окончания заметки
    print('Сегодня')
    print(f'{today:%d-%m-%Y}', ' Пожалуйста, введите дату окончания заметки')

    while True:
        try:
            issue_date = input(
                'Введите дату дедлайна (в формате xx-xx-xxxx)\n')  # ввод даты пользователя  формате дд-мм-гггг
            issue_date = datetime.strptime(issue_date, '%d-%m-%Y')
            issue_date = datetime.strftime(issue_date, '%d-%m-%Y')
            break
        except:
            print('Введен невеный формат даты, попробуйте еще раз ')
    note1.update(issue_date=issue_date)
    print('Дата окончания заметки: ', note1['issue_date'])
    notes_list.append(note1)
    for note in notes_list:
        print(note)