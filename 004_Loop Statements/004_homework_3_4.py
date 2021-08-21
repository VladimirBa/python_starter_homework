H = int(input('Высота "левого" прямоугольного треугольника: '))
i = 0
while i < H:
    j = 0
    while i + 1 > j:
        if j <= H - 1:
            print('*', end='')
            j += 1
        else:
            print(' ', end='')
            j += 1
    i += 1
    print()
