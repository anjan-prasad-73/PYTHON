num=5
k=2
num=(num<<k) | (num>>(32-k))
print(num)