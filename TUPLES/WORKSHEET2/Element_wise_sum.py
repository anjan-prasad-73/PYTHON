t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)

result = tuple(sum(x) for x in zip(t1, t2, t3))
print(result)  


mul = 1

for num in t1:
    mul *= num

print(mul)