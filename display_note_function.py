from datetime import datetime



notes_list = []
note = {
    'username': 'Алексей',
    'title': 'Список покупок',
    'content': 'Купить продукты',
    'status': 'новая',
    'created_date': datetime.strftime(datetime.today(),'%d-%m-%Y'),
    'issue_date': '30-11-2025'
}


notes_list.append(note)


def display_notes():
    print(notes_list)
    return