height = int(input("Высота \"левого\" прямоугольного треугольника: "))
for row in range(height):
    for column in range(height):
        if row + 1 > column:
            print('*', end="")
        else:
            print(' ', end="")
    print()
