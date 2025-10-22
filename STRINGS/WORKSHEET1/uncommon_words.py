s1 = "red blue green".split()

s2 = "blue yellow red".split()

uncommon = list(set(s1) ^ set(s2))

print("Uncommon:", uncommon)  
