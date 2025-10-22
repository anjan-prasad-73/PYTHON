t = ((1, 2), (3, 4), (5, 6))

flat = tuple(x for sub in t for x in sub)

print(flat)
