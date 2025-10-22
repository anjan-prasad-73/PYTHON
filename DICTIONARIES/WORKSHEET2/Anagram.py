words = ['listen', 'silent', 'enlist', 'hello', 'ohlle']
from collections import defaultdict

groups = defaultdict(list)
for w in words:
    key = tuple(sorted(w))
    groups[key].append(w)

print(list(groups.values()))


num1 = 5  
num2 = 6  

is_anagram = sorted(bin(num1)[2:]) == sorted(bin(num2)[2:])
print(is_anagram)
