# создание статуса заметки
status = None
status_accept = None

print('Текущий статус заметки: В процессе')
print('Для сменый статуса нажмите одну из приведенных цифр\n'
      '1 - Выполнено\n'
      '2 - В процессе\n'
      '3 - Отложено')

# def status_maker(status_accept,status):
#     if status_accept == 'нет' or status_accept == 'ytn':
#         print('Статус сохранен на: ', status)
#         break
#     if status_accept == 'да' or status_accept == 'lf':
#         print('Текущий статус заметки: ', status)
#         print('Для сменый статуса нажмите одну из приведенных цифр\n'
#             '1 - Выполнено\n'
#             '2 - В процессе\n'
#             '3 - Отложено\n')


while True: # цикл перезаписи значения для status
    try:
        status_changer = abs(int(input()))
        if status_changer == 1: # вариант для значения 1
            status = 'Выполнено'
            print('Статус изменен на: ', status)
            status_accept = input('Изменить статус заметки(да / нет)?\n').lower() # уточнение для изменения статуса
            try:
                status_maker(status_accept,status)
            except:
                print('Пожалуйста, введите да или нет')
        elif status_changer == 2: # вариант для значения 2
            status = 'В процессе'
            print('Статус изменен на: ', status)
            status_accept = input('Изменить статус заметки(да / нет)?\n').lower()
            try:
                status_maker(status_accept,status)
            except:
                print('Пожалуйста, введите да или нет')
        elif status_changer == 3: # вариант для значения 3
            status = 'Отложено'
            print('Статус изменен на: ', status)
            status_accept = input('Изменить статус заметки(да / нет)?\n').lower()
            try:
                status_maker(status_accept, status)
            except:
                print('Пожалуйста, введите да или нет')
        else:
            while status_changer < 1 or status_changer > 3: # исключение ошибки
                print('Убедитесь в правильности ввода')
                break
    except:
        print('Пожалуйста повторите ввод используя цифры')
