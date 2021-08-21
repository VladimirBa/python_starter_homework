import math

x = float(input('Введите значение аргумента х для функции y = f(x): '))
y = math.cos(x)
y if -3.1416 <= x <= 3.1416 else x
print(f'{y:.3f}')
