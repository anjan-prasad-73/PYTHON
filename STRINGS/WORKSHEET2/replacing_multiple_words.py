s = "I like apples and bananas."

replacements = {"apples": "oranges", "bananas": "grapes"}

for old, new in replacements.items():
    s = s.replace(old, new)
    
print(s) 
