led1,led2,led3 = 0,1,0

if led1 and led2 and led3:
    print("All LEDs are ON")
elif led1 and led2:
    print("LED1 and LED2 are ON")
elif led2 and led3:
    print("LED2 and LED3 are ON")
elif led1 and led3:
    print("LED1 and LED3 are ON")
elif led1:
    print("LED1 is ON")
elif led2:
    print("LED2 is ON")
elif led3:
    print("LED3 is ON")
else:
    print("All LEDs are OFF")