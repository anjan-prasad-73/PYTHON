s = "my_variable_name"

pascal = "".join(word.capitalize() for word in s.split("_"))

print(pascal)  