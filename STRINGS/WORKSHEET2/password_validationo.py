import re
password = "MyPass123!"

valid = len(password) >= 8 and bool(re.search(r"[A-Za-z]", password)) and bool(re.search(r"\d", password)) and bool(re.search(r"[!@#$%^&*()]", password))
print("Valid password:", "Yes" if valid else "No")  
