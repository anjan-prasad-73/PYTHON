lst = [1,2,3,4,5,6]
pos = 3

lst[pos:] = lst[pos:][::-1]
print(lst) 


