from datetime import datetime
import json



notes_list = []
file = open('filename.txt','w',encoding='UTF-8')

username = input('Имя пользователя: ')
title = input('Заголовок: ')
content = input('Описание: ')
status = input('Статус: ')
created_date = datetime.strftime(datetime.today(),'%d-%m-%Y')
issue_date = input('Дата окончания заметки: ')


note1 = {
    'username' : username,
    'title' : title,
    'content' : content,
    'status' : status,
    'created_date' : datetime.strftime(datetime.today(),'%d-%m-%Y'),
    'issue_date' : issue_date}
notes_list.append(note1)
note = [
    {
        "username": "Алексей",
        "title": "Список покупок",
        "content": "Купить продукты",
        "status": "новая",
        "created_date": "27-11-2024",
        "issue_date": "30-11-2024"
    }
]
notes_list.append(note)


def save_note_to_file(note1, file = open('filename.txt','w',encoding='UTF-8')):
    file.write(str(note1))
    file.close()


def load_notes_from_file(file = open('filename.txt','r',encoding='UTF-8')):
    print(file.read())
    file.close()
    return

def append_notes_to_file(notes_list, file = open('filename.txt','a',encoding='UTF-8')):
    file.write(notes_list)
    file.close()

def save_notes_json(notes_list, file = open('filename.txt','x',encoding='UTF-8')):
    j_file = json.dumps(notes_list,file,indent=4,ensure_ascii=False)
    file.close()


try:
    save_note_to_file(note1,file)
except FileNotFoundError:
    print('Файл отсутствует или не был найден'
          'Проверьте имя или директорию')
except PermissionError:
    print('Доступ к файлу ограничен')
load_notes_from_file(file)
append_notes_to_file(notes_list, file)