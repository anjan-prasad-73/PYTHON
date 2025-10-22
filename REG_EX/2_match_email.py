import re

email = "user@example.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
print(bool(re.match(pattern, email)))  
