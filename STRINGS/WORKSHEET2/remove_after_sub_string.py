s = "abcdeFGhiJK"
sub = "FG"

pos = s.find(sub)
s_new = s[:pos+len(sub)]

print(s_new) 