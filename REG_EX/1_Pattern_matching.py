import re

text = "Hello, World! $51.413 and 52.8, $60.21"

pattern = '\$([0-9\.]+)'

for match in re.findall(pattern,text):
    print(match)