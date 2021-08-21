a = list(input("Your text: ").lower())


def sort_():
    for i in a:
        if i in (',', '.', ':', '-', ';', '!', '?', '"'):
            a.remove(i)
    b = "".join(a)
    b = b.split()
    b.sort()
    print(' '.join(b))


sort_()
