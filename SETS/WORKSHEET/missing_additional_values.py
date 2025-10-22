old_hw = ["math", "science", "art"]
new_hw = ["math", "history", "science"]

missing = set(old_hw) - set(new_hw)
additional = set(new_hw) - set(old_hw)
print("Missing:", missing.pop())
print("Additional:", additional.pop())
