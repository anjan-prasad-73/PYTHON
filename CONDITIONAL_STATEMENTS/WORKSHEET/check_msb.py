reg = 0b10010010

if reg & 0b10000000:
    print("MSB set")
else:
    print("MSB not set")
