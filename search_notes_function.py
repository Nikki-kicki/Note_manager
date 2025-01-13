from datetime import datetime




notes_list = []
note1 = {
    'username' : 'Анастасия',
    'title' : 'Домашнее задание',
    'content' : 'Создать функцию поиска данных заметки',
    'status' : 'В процессе',
    'created_date' : datetime.strftime(datetime.today(),'%d-%m-%Y'),
    'issue_date' : 'Дата завершения'}
notes_list.append(note1)

note2 = {
    'username' : 'Мирон',
    'title' : 'Планы на 2025',
    'content' : 'Создать функцию обновления данных заметки',
    'status' : 'Отложено',
    'created_date' : datetime.strftime(datetime.today(),'%d-%m-%Y'),
    'issue_date' : 'Дата завершения'}
notes_list.append(note2)


print('Здравствуйте это программа поиска данных о записке')

def search_notes(notes, keyword = None, status = None):
    while True:
        if notes == '' or notes == ' ':
            print('Пожалуйста заполните значение')
            break
        keyword = input('Введите доп. заголовки или оставтье поле пустым\n')
        if keyword == '' or keyword == ' ':
            keyword = None
        status = input('Введите статус заметки или оставтье поле пустым\n')
        if status == '' or status == ' ':
            status = None
        for note in notes_list: # цикл распаковки где из списка словарей(заметок) выводятся сами словари
            for key in note.values(): # вложеный цикл где из словаря(заметки) выводятся значения заполненные пользователем
                if key == notes or key == keyword or key == status: # сравнивание того что ищем со списком значений введенных в заметку
                    print('есть сходство в',note,' значение: ',key) # вывод заметки(словаря) где было найдено значение
                    break
        break
notes = input('Введите заголовок\n')
search_notes(notes)