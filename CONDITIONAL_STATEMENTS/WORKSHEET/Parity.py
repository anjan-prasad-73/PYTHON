val = 0xAAAA

parity = bin(val).count('1') % 2

print("Parity: Even" if parity == 0 else "Parity: Odd")
