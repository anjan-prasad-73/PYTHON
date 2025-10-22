voltage = float(input("Enter the voltage: "))

if voltage < 10:
    print("Under voltage")
elif voltage < 20:
    print("Nominal")
else:
    print("Over voltage")