d = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 5, 'Five': 6}


def func(**kwargs):
    for key in kwargs:
        print("Key", key, 'has value', kwargs.get(key))


func(**d)

print()

func(One=1, Two=2, Three=3, Four=5, Five=6)
