import copy

original = {'car': 'red', 'bike': 'blue'}
copy_d = original.copy()
copy_d['car'] = 'green'
print(original) 
print(copy_d)    

nested = {'x': [1, 2, 3]}
shallow = nested.copy()
deep = nested

shallow['x'].append(4)
print(nested)  

deep['x'].append(5)
print(nested)  