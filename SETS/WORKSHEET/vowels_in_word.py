words = ["education", "python", "sequoia"]
vowels = set('aeiou')

result = [w for w in words if vowels <= set(w)]

print(result)
