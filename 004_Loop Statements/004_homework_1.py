for i in range(101):
    if i == 4:
        continue
    elif i == 18:
        break
    print(f"i = {i:2d}")

i = 0
while i <= 100:
    if i == 4:
        i += 1
        continue
    elif i == 18:
        break
    print(f"i = {i:2d}")
    i += 1
