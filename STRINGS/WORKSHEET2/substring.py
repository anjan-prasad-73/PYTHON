s = "abracadabra"
sub = "abra"

indices = [i for i in range(len(s)) if s.startswith(sub, i)]

print(indices)  