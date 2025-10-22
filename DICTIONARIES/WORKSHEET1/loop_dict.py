d = {'a': 10, 'b': 20, 'c': 30}

for k in d:
    print(k)

for v in d.values():
    print(v)


for k, v in d.items():
    print(k, v)

scores = {'math': 75, 'science': 55, 'english': 82}
for subject, mark in scores.items():
    if mark > 60:
        print(subject)
