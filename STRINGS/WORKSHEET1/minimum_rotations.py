s = "abcde"
for i in range(1, len(s)+1):
    if s[i:]+s[:i] == s:
        print("Minimum rotations:", i)  
        break
