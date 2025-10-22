lst = [1, 2, 3, 4]
clone = lst.copy()
print(clone) 

clone[0] = 5
print(clone)
print(lst)
 # a new list is created

new_lst = lst
print(new_lst)
print(lst)
#this creates a reference not the copy

new_lst[0] = 10
print(new_lst)
print(lst)