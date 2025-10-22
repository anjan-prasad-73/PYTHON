d = {'hello': 1, 'world': 2, 'hell': 3}
substring = 'hell'

keys_found = [k for k in d if substring in k]

print("Keys containing 'hell':", keys_found)
