def gcd(number1, number2):
    return number1 if not number2 else gcd(number2, number1 % number2)


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("НОД =", gcd(num1, num2))
