sound = input('Введите звук, который издаёт животное: ')

if sound.lower() == 'meow':
    print('Это животное - Кошка.')
elif sound.lower() == 'bark':
    print('Это животное - Собака.')
else:
    print('Неизвестный зверь')
