s = "abcdefgh"
n = 3
groups = [s[i:i+n] for i in range(0, len(s), n)]
print(groups) 
