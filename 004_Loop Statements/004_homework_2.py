STRING = "Hello, World!"
i = 0
while i in range((len(STRING) - 1)):
    if STRING[i] == 'o':
        print("a", end=' ')
        i += 1
    elif STRING[i] == 'l':
        print('e', end=' ')
        i += 1
    else:
        print(STRING[i], end=' ')
        i += 1

STRING = "Hello, World!"
for i in range(0, len(STRING)):
    if STRING[i] == 'o':
        print("a", end=' ')
    elif STRING[i] == 'l':
        print('e', end=' ')
    else:
        print(STRING[i], end=' ')
