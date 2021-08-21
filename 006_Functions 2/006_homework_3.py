def steps():
    a = b = 1
    n = int(input("Введите количество ступенек: ")) - 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    print("Количество способов:", b)


def main():
    steps()


if __name__ == '__main__':
    main()
