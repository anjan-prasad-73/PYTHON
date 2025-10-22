def string_stats(s):
    vowels = "aeiouAEIOU"
    v = c = d = 0
    for ch in s:
        if ch.isdigit():
            d += 1
        elif ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return (v, c, d)

print(string_stats("Hello123"))
