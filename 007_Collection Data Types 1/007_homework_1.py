a = [2, 4, 65, 32, 2, 6, 0, -1, 3]
b = []


def five():
    for i in a:
        if i < 5:
            b.append(i)
    print(b)


five()
