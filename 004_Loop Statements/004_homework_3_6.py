H = int(input("Высота равнобедренного треугольника: "))
for i in range(H):
    for j in range(2 * H - 1):
        print('*', end="") if H - i - 1 <= j <= H + i - 1 else print(" ", end='')
    i += 1
    print()
