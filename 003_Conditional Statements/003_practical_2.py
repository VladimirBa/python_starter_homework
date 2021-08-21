X_ODD_MESSAGE = "нечётное"
X_EVEN_MESSAGE = "чётное"
X_NEGATIVE_MESSAGE = "отрицательное"
X_POSITIVE_MESSAGE = "положительное"

x = float(input("Введите число: "))
x_length = len(str(abs(int(x))))

if x == 0:
    print('Число: ', x)
elif x % 2 == 0 and x < 0:
    print(x, f"{X_EVEN_MESSAGE} {X_NEGATIVE_MESSAGE} число.", end=" ")
elif x % 2 != 0 and x < 0:
    print(x, f"{X_ODD_MESSAGE} {X_NEGATIVE_MESSAGE} число.", end=" ")
elif x % 2 == 0 and x > 0:
    print(x, f"{X_EVEN_MESSAGE} {X_POSITIVE_MESSAGE} число.", end=" ")
elif x % 2 != 0 and x > 0:
    print(x, f"{X_ODD_MESSAGE} {X_POSITIVE_MESSAGE} число.", end=" ")

print(f"Знаков перед запятой: {x_length}" if x else "")
