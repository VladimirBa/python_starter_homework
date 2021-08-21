a = "a14b6fh"

set_a = set(a)
print("Elements of the string are unique.") if len(a) == len(set(a)) else print("Elements of the string are not unique.")
