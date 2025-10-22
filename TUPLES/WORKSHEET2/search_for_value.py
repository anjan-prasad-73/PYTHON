t = (('Red', 'White', 'Blue'),
     ('Green', 'Pink', 'Purple'),
     ('Orange', 'Yellow', 'Lime'))

check = 'White'
result = any(check in inner for inner in t)
print(result)  
