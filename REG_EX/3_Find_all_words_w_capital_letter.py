import re

text = "Python is Great and Powerful"
print(re.findall(r"\b[A-Z]\w*", text))  
