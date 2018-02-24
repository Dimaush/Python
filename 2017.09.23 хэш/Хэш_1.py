def LOL (x):
    #y = (- 4 * x ** 3 + 129 * x ** 2 - 1373 * x) // 6 + 806
    return (y)

a1 = input ()
a2 = input ()
a3 = input ()
s = a1 + ' ' + a2 + ' ' + a3
le = len (s)
p = '0' * le
#g = [0, 0, 0]
n = '0123456789'
l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = 0
for i in range (le):
    p = p [:i] + str (2 * n.count (s [i]) + l.count (s [i])) + p [i + 1:]
    #p [i] = 2 * n.count (s [i]) + l.count (s [i])
    #if p [i] != 0: g [t] += p [i] * 10 ** (i - len (a1) * min (t, 1) - len (a2) * min (max (0, t - 1), 1))
    #else: t += 1
#g [0], g [1], g [2] = int (str (g [0]) [::-1]), int (str (g [1]) [::-1]), int (str (g [2]) [::-1])
#print (g)
b1, b2, b3 = p [:len (a1)], p [len (a1) + 1:len (a1) + 1 + len (a2)], p [len (a1) + 2 + len (a2):]
#c1, c2, c3 = sum (b1) + b1 [0], sum (b2) + b2 [0], sum (b3) + b3 [0]
#print (max (0, LOL (c1)), max (LOL (c2), 0), max (LOL (c3), 0))
M = [b1, b2, b3]
for i in range (3):
    if M [i] == '122211': print (1)
    elif M [i] == '11222': print (2)
    elif M [i] == '112222': print (3)
    elif M [i] == '222211': print (4)
    else: print (0)

#AB179
#Y068IJ
#FG3468
