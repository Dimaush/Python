L = input ().split ()
n = len (L)
S = []
for i in range (n):
    t = L [i]
    if t.isdigit (): S.append (t)
    else:
        k = int (S.pop ())
        l = int (S.pop ())
        if t == '+': S.append (k + l)
        elif t == '-': S.append (l - k)
        elif t == '*': S.append (k * l)
print (S [0])