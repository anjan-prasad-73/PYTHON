msg = "hello world"
vowels = {'a','e','i','o','u'}

count = sum(1 for ch in msg if ch in vowels)

print(count)
