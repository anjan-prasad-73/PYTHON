import string

s = "Hello, world! How are you?"

s_clean = "".join(ch for ch in s if ch.isalnum() or ch.isspace())

print(s_clean)  
    