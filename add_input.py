from datetime import datetime

# ввод данных и вывод результата
username = ('Пользователь: ',input('Введите имя пользователя:\n'))
title = ('Заголовок заметки',input('Введите название заметки:\n'))
content = ('Описание заметки',input('Введите описание заметки:\n'))
status = ('Статус заметки',input('Назначьте статус заметки:\n'))
print('Дата создания заметки')
created_date = datetime.strptime(input('Введите дату создания заметки в формате xx.xx.xxxx: \n'),'%d.%m.%Y')
print('Дата истечения заметки')
issue_date = datetime.strptime(input('Введите дедлайн(дату истечения) заметки в формате xx.xx.xxxx: \n'),'%d.%m.%Y')

