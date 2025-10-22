import random
import string

target = "abc"
attempts = 0
while True:
    attempts += 1
    rand_str = "".join(random.choice(string.ascii_lowercase) for _ in range(len(target)))
    if rand_str == target:
        break
print(f"Generated '{target}' after {attempts} attempts")
