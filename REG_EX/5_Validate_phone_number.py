import re

phone = "+91 1234567890"
pattern = r"^\+\d{2} \d{10}$"

for number in re.findall(pattern, phone):
    print(number)


