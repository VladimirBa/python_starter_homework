H = int(input('Высота "правого" прямоугольного треугольника: '))
i = 0
while i < H:
    j = 0
    while j < H:
        if j <= H - i - 2:
            print(' ', end='')
            j += 1
        else:
            print('*', end='')
            j += 1
    i += 1
    print()
