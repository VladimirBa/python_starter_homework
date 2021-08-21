import math

x = float(input('Введите первое число: '))
d = input('Введите тип операции над числами (+, -, *, /, sin, cos, tan): ')
if d == str('sin'):
    print(f"Результат: {(math.sin(x)):.3f}")
elif d == str('cos'):
    print(f"Результат: {(math.cos(x)):.3f}")
elif d == str('tan'):
    print(f"Результат: {(math.tan(x)):.3f}")

else:
    y = float(input('Введите второе число: '))
if d == "/" and y == 0:
    print("Деление на ноль невозможно. Введите другое второе число y: ")
    y = float(input('Введите второе число: '))
    print(f"Результат: {(x / y):.3f}")
else:
    if d == str('+'):
        print(f"Результат: {(x + y):.3f}")
    elif d == str('-'):
        print(f"Результат: {(x - y):.3f}")
    elif d == str('*'):
        print(f"Результат: {(x * y):.3f}")
    elif d == str('/'):
        print(f"Результат: {(x / y):.3f}")
    elif d == str('**'):
        print(f"Результат: {(x ** y):.3f}")
