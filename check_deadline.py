#from greetings import issue_date
#import re
from datetime import datetime,timedelta

#pattern = r"(\d{2})[^0-9]?[ ]?(\d{2})[^0-9]?[ ]?(\d{4})";
today = datetime.today() # переменная хранит сегодняшнюю дату
print('Сегодня')
print(f'{today:%d-%m-%Y}')

while True:
    try:
        issue_date = input('Введите дату дедлайна (в формате день-месяц-год)\n') # ввод даты пользователя  формате дд-мм-гггг
        issue_date = datetime.strptime(issue_date, '%d-%m-%Y') # ввод даты пользователя  формате дд-мм-гггг
        break
    except:
        print('Введен невеный формат даты')


if issue_date > today: # сравниваем для определенного вывода
    result = issue_date - today # проверяем разницу для определенного вывода
    if result < timedelta(days=5) and result != 1: # если значение меньше 5 и не равняется 1 то пишем дня(осталось 2 дня)
        print('Внимание до делайна осталось: ',result.days,' дня')
    elif result == 1: # если значение 1 то пишем день(остался один день)
        print('Внимание до делайна осталось: ', result.days, ' день')
    else: # если значение больше или равно 5 то пишем дней(осталось 6 дней)
        print('Внимание до делайна осталось: ', result.days, ' дней')
elif issue_date < today:
    result = today - issue_date
    if result < timedelta(days=5) and result != 1:
        print('!!! Дедлайн истек ',result.days,' дня назад')
    elif result == 1:
        print('!!! До дедлайна ', result.days, ' один день')
    else:
        print('!!! Дедлайн истек ', result.days, ' дней назад')
elif issue_date == today:
    print('сегодня последний день')
else:
    print('Что то пошло не так')
