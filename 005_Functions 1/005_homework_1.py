def hello(name):
    print('Привет, ', name, "!", sep='') if name else print('Привет, Вова!')
    return


name = input("Введите Ваше имя: ")


hello(name)
