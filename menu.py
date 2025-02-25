from datetime import datetime
from create_note_function import create_note
from update_note_function import update_note
from delete_note_function import delete_note
from search_notes_function import search_notes


notes_list = []
note1 = {
    'username': 'Алексей',
    'title': 'Список покупок',
    'content': 'Купить продукты',
    'status': 'новая',
    'created_date': datetime.strftime(datetime.today(),'%d-%m-%Y'),
    'issue_date': '30-11-2025'}
note2 = {
    'username' : 'Анастасия',
    'title' : 'Домашнее задание',
    'content' : 'Создать функцию обновления данных заметки',
    'status' : 'В процессе',
    'created_date' : datetime.strftime(datetime.today(),'%d-%m-%Y'),
    'issue_date' : '12-10-26'}


print('Вас приветствует менеджер заметок\nВыберите необходимое действие!')
print('1. Создать новую заметку'
      '2. Показать все заметки'
      '3. Обновить заметку'
      '4. Удалить заметку'
      '5. Найти заметки'
      '6. Выйти из программы')

choice = int(input('Введите число: '))

while True:
    try:
        choice = int(input('Введите число: '))
        if choice == 1:
            create_note()
            continue
        elif choice == 2:
            print(notes_list)
            continue
        elif choice == 3:
            update_note()
            continue
        elif choice == 4:
            delete_note()
            continue
        elif choice == 5:
            notes = input('Введите заголовок\n')
            search_notes(notes)
            continue
        elif choice == 6:
            print('Хорошо, мы закончили')
            break
        else:
            print(f'Пожалуйста введите число для необходимого действия. Ваш выбор: ', {choice})
    except ValueError:
        print('Пожалуйста введите число')