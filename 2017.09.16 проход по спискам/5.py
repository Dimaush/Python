M = list (map (int, input ().split ()))
print ()
M.sort ()
l = len (M)
P = []
#K = []
lenght = 0
for i in range (l):
    x = M [i]
    x1 = 2 * x
    a = i #-----------------------------------> Бинпоиск
    b = l - 1 #-------------------------------> Бинпоиск
    while b - a > 1: #------------------------> Бинпоиск
        c = (a + b) // 2 #--------------------> Бинпоиск
        if M [c] > x1: b = c #----------------> Бинпоиск
        else: a = c #-------------------------> Бинпоиск
    if M [b] <= x1:
        #K.append (M [i:b + 1])
        if b + 1 - i > lenght:
            lenght = b + 1 - i
            P = []
            P.append (M [i:b + 1])
        elif b + 1 - i == lenght: P.append (M [i:b + 1])
    else:
        #K.append (M [i:a + 1])
        if a + 1 - i > lenght:
            lenght = a + 1 - i
            P = []
            P.append (M [i:a + 1])
        elif a + 1 - i == lenght: P.append (M [i:a + 1])
#print (K)
for i in range (len (P)): print (*P [i])