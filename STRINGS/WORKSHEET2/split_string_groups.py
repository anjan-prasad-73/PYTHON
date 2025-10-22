s = "abcdefgh"
n = 3
groups = [s[i:i+n] for i in range(0, len(s), n)]
print(groups) 

s = "abracadabra"
sub = "abra"
indices = [i for i in range(len(s)) if s.startswith(sub, i)]
print(indices)  
