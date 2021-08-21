def pol_om():
    pol = list(input("Введите слово для проверки на полиндром: ").lower())
    if list(pol) == list(reversed(pol)):
        print("Полиндром")
    else:
        print("Не полиндром")


def main():

    pol_om()


if __name__ == "__main__":
    main()
