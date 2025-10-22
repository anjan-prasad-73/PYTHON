from itertools import combinations
kids = {"Amy", "Bob", "Cara", "Dan", "Eva"}
size = 3

for team in combinations(kids, size):
    print(team)
    break 