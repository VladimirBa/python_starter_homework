import math

r = float(input('Введите радиус круга в см: '))
S = math.pi * r ** 2
print('Площадь круга радиусом', r, 'см равна,', round(S, 2), 'кв. см.')
