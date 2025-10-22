import re

text = "Order 66 costs 250 and delivery 30"
print(re.findall(r"\d+", text))  
