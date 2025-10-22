t = (('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'))

result = sorted(t, key=lambda x: float(x[1]), reverse=True)

print(result)  

