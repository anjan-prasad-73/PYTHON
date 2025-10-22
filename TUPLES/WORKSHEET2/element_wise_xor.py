t1 = (1, 2, 3)
t2 = (2, 2, 2)

and_result = tuple(a & b for a, b in zip(t1, t2))
xor_result = tuple(a ^ b for a, b in zip(t1, t2))

print("AND:", and_result) 
print("XOR:", xor_result)  
