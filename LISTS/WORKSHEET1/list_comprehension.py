fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [f for f in fruits if "a" in f]
print(newlist)   

upperlist = [f.upper() for f in fruits]
print(upperlist)

replaced = ["orange" if f == "banana" else f for f in fruits]
print(replaced)
