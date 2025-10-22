words = ['hello', 'world', 'python', 'is', 'great']
n = 4

long_words = [w for w in words if len(w) > n]
print(long_words)  