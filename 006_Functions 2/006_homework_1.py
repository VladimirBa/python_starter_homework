z = 0
print(z)


def greeting(z):
    while z < 2:
        print('Hello!')
        z += 1
    print(z)


greeting(z)


def out_f():
    x = 1

    def inn_f():
        global x
        print(x)
        x = 2
        print(x)

    inn_f()
    print(x)

    def in_inn_f():
        nonlocal x
        x = 3

    print(x)
    in_inn_f()
    print(x)


x = 10
print(x)
out_f()
print(x)
