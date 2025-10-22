a = 10
b = 5

result = 0

while b > 0:
    if b & 1:
        result += a

    a <<= 1
    b >>= 1

print(result)