word1 = "apple"
word2 = "orange"

uncommon = set(word1) ^ set(word2)

print("".join(uncommon))
