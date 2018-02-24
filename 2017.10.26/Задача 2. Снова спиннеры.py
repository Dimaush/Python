M = int (input ())
if M == 1 or M == 2 or M == 5:
    print (0)
    print (0)
else:
    x = 0
    while M % 3 != 0:
        M -= 4
        x += 1
    print (M // 3)
    print (x)