from datetime import datetime


note_list = []
note1 = {
    'username' : 'Анастасия',
    'title' : 'Домашнее задание',
    'content' : 'Создать функцию обновления данных заметки',
    'status' : 'В процессе',
    'created_date' : datetime.strftime(datetime.today(),'%d-%m-%Y'),
    'issue_date' : 'Дата завершения'}

def update_note():
    while True:
        try:
            print('Здравствуйте, введите поле которое хотите обновить(дату создания обновить нельзя)')
            print(note1.keys())
            key = input().lower()
            if key in ['username','title','content','status','issue_date']:
                print('Меняем: ', key)
                if key == 'issue_date':
                    print('Введите дату окончания заметки в формате дд-мм-гггг')
                    issue_date = datetime.strptime(input(),'%d-%m-%Y')
                    issue_date = datetime.strftime(issue_date,'%d-%m-%Y')
                    note1.update(issue_date=issue_date)
                    print(f'Теперь {key}: {issue_date}')
                    break
                elif key == 'username':
                    print('Пожалуйста введите новое имя пользователя')
                    username = input()
                    if username == '' or username == ' ':
                        print('Это поле должно быть заполнено')
                        continue
                    else:
                        note1.update(username=username)
                        print(f'Теперь {key}: {username}')
                        break
                elif key == 'title':
                    title = input(
                        'Можете ввести заголовок или оставьте поле пустым для остановки\n')  # Просим ползователя ввести данные
                    if title == '' or title == ' ':  # Проверяем данные пользователя где пустое значение остановит цикл
                        break
                    elif title == note1.get('title'):  # проверка на уникальность данных
                        print('Такой заголовок уже есть', title)
                        continue
                    else:
                        note1.update(title=title)  # Добавление значения в список через метод .append
                        break
                elif key == 'status':
                    status = None
                    status_accept = None

                    print('Текущий статус заметки: В процессе')
                    print('Для смены статуса нажмите одну из приведенных цифр\n'
                          '1 - Выполнено\n'
                          '2 - В процессе\n'
                          '3 - Отложено')

                    while True:  # цикл перезаписи значения для status
                        try:
                            status_changer = abs(int(input()))
                            if status_changer == 1 and status_changer != '' or ' ':  # вариант для значения 1
                                status = 'Выполнено'
                                print('Статус изменен на: ', status)
                                status_accept = str(input(
                                    'Изменить статус заметки(да / нет)?\n').lower())  # уточнение для изменения статуса
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
                    break
                elif key == 'content':
                    print('Добавтье до 3-ех ключевых слов(ничего не вводите для пропуска)')

                    num = 0
                    key_list = []

                    while num < 3:
                        key_title1 = input('Основные темы ')
                        if key_title1 == '' or key_title1 == ' ':
                            num += 1
                            key_title1 = None
                        else:
                            num += 1
                            key_list.append(key_title1)
                        key_title2 = input('Персонажи ')
                        if key_title2 == '' or key_title2 == ' ':
                            num += 1
                            key_title2 = None
                        else:
                            num += 1
                            key_list.append(key_title2)
                        key_title3 = input('Рекомендации для чтения ')
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
                else:
                    print('Пожалуйста введите дату согласно шаблону')
                    continue
            else:
                print('Убедитесь в правильности ввода')
                continue
        except:
            print('Что-то пошло не так')

update_note()
print(note1)