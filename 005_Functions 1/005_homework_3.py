def cont():
    c = input("Хотите прекратить вычисления? Если Да, введите Y: ")
    while True:
        if c == "Y":
            return None
        else:
            return main()


def div(d, x, y):
    if y == 0:
        y = input("Деление на ноль невозможно. Введите другое второе число y: ")
        y = float(y)
        div(d, x, y)
    else:
        print(f"Результат: {(x / y):.3f}")


def mul(x, y):
    print(f"Результат: {(x * y):.3f}")


def add(x, y):
    print(f"Результат: {(x + y):.3f}")


def sub(x, y):
    print(f"Результат: {(x - y):.3f}")


def main():
    x = float(input('Введите первое число: '))
    d = input('Введите тип операции над числами: ')
    y = float(input('Введите второе число: '))
    if d == '/':
        div(d, x, y)
    elif d == '*':
        mul(x, y)
    elif d == '+':
        add(x, y)
    elif d == '-':
        sub(x, y)
    cont()


if __name__ == "__main__":
    main()
