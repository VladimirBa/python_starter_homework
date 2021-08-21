height = int(input("Высота \"правого\" прямоугольного треугольника: "))
for row in range(height):
    for column in range(height):
        if height - row < column + 2:
            print('*', end="")
        else:
            print(' ', end="")
    print()
