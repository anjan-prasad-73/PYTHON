nested = (('1','2'), ('3','4'))

nums = tuple(tuple(int(x) for x in inner) for inner in nested)

print(nums)
