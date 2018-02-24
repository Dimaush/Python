n = input ()
l = len (n)
s = 0
for i in range (l): s += int (n [i])
s1 = 3 - s % 3
for i in range (l):
    p = int (n [i]) + s1
    if p < 10:
        p += (9 - p) // 3 * 3
        n = n [:i] + str (p) + n [i + 1:]
        print (n)
        break
    elif i == l - 1:
        p = int (p - 1.5 * s1 ** 2 + 4.5 * s1 - 6)
        n = n [:-1] + str (p)        
        print (n)