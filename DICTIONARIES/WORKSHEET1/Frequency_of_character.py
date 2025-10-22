word = "apple"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)   
