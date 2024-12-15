

print('Добавтье до 3-ех ключевых слов')


key_title1 = input()
if key_title1:
    print('Добавим еще?')
    key_title2 = input()
    if key_title2:
        print('И еще одно')
        key_title3 = input()
        if key_title3:
            print('Добавлено максимальное количество ключевых слов')

key_list = [key_title1,key_title2,key_title3]

print('Это ваши ключевые слова:')
print(key_list)