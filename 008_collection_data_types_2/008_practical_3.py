d = {'a': 3, 'b': 'hello', 'c': 4, 'd': -3}
d_list = list(d.values())
a_e_list = []
b_e_list = []

for i in d_list:
    if type(i) == int:
        a_e_list.append(i)
    else:
        b_e_list.append(i)
print("Максимальное числовое значение словаря d: ", max(a_e_list))
print("Максимальное не числовое значение словаря d: ", max(b_e_list))
