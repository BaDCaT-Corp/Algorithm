print( '7. Определить, является ли год, который ввел пользователь, високосным или не високосным.')

year = int(input('Введите год:'))
if ( year % 4 ) != 0:
    print('Обычный год')
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Високосный')
        else:
            print('Обычный')
    else:
        print('Високосный')