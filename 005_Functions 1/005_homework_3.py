def cont():
    c = input("Do you want to stop computing? Enter Y if yes: ")
    while True:
        if c == "Y":
            return None
        else:
            return main()


def div(x, y):
    if y == 0:
        y = input("Division by zero is not possible. Please enter another second number y: ")
        y = float(y)
        div(x, y)
    else:
        print(f"Result: {(x / y):.3f}")


def mul(x, y):
    print(f"Result: {(x * y):.3f}")


def add(x, y):
    print(f"Result: {(x + y):.3f}")


def sub(x, y):
    print(f"Result: {(x - y):.3f}")


def main():
    x = float(input('Enter the first number: '))
    d = input('Enter the type of operation on numbers: ')
    y = float(input('Enter the second number: '))
    if d == '/':
        div(x, y)
    elif d == '*':
        mul(x, y)
    elif d == '+':
        add(x, y)
    elif d == '-':
        sub(x, y)
    cont()


if __name__ == "__main__":
    main()
