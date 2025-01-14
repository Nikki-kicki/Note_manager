# создание статуса заметки
status = None
status_accept = None

print('Текущий статус заметки: В процессе')
print('Для сменый статуса нажмите одну из приведенных цифр\n'
      '1 - Выполнено\n'
      '2 - В процессе\n'
      '3 - Отложено')


while True: # цикл перезаписи значения для status
    try:
        status_changer = abs(int(input()))
        if status_changer == 1: # вариант для значения 1
            status = 'Выполнено'
            print('Статус изменен на: ', status)
            status_accept = input('Изменить статус заметки(да / нет)?\n').lower() # уточнение для изменения статуса
        elif status_changer == 2: # вариант для значения 2
            status = 'В процессе'
            print('Статус изменен на: ', status)
            status_accept = input('Изменить статус заметки(да / нет)?\n').lower()
        elif status_changer == 3: # вариант для значения 3
            status = 'Отложено'
            print('Статус изменен на: ', status)
            status_accept = input('Изменить статус заметки(да / нет)?\n').lower()
        else:
            while status_changer < 1 or status_changer > 3: # исключение ошибки
                print('Убедитесь в правильности ввода')
                break
    except:
        print('Пожалуйста повторите ввод используя цифры')
