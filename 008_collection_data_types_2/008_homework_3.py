c = {'a': 'as', 'b': 'z', 'c': 'for', 'd': 'A'}
print("clear:", c.clear())
c = {'a': 'as', 'b': 'z', 'c': 'for', 'd': 'A'}
print("items:", c.items())
print("pop 'b':", c.pop('b'))
print("popitem:", c.popitem())
c.update({'e': 2, 'd': -9})
print("update :", c)
print("values:", c.values())
