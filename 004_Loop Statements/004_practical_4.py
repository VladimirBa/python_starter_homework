H = int(input("Высота равнобедренного треугольника: "))
i = 0
while i < H:
    j = 0
    while j < 2 * H - 1:
        if H - i - 1 <= j <= H + i - 1:
            print("*", end='')
            j += 1
        else:
            print(" ", end='')
            j += 1
    i += 1
    print()
