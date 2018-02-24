A = list (map (int, input ().split ()))
B = list (map (int, input ().split ()))
A0, B0 = A [:], B [:]
s = 0
flag = 0
while len (A) > 0 and len (B) > 0 and flag == 0:
    a, b = A.pop (0), B.pop (0)
    X = [a, b]
    if a == 0 and b == 9: A += X
    elif a == 9 and b == 0: B += X
    elif a > b: A += X
    else: B += X
    if A == A0:
        flag = 1
    else: s += 1
if len (A) == 10: print ('first', s)
elif len (B) == 10: print ('second', s)
else: print ('botva')