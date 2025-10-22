lst = ["applebanana", "apple", "banana", "applebananacherry"]

substrings = ["apple", "banana"]

filtered = [item for item in lst if all(sub in item for sub in substrings)]

print(filtered)  
