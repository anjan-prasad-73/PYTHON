import re

s = "Check https://openai.com and http://github.com"

urls = re.findall(r'https?://\S+', s)

print("URLs found:", urls)
