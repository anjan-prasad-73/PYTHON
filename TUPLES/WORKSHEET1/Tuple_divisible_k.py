lst = [(3, 6), (9, 12, 15), (4, 8)]

K = 3

count = sum(1 for t in lst if all(x % K == 0 for x in t))

print(count)  
