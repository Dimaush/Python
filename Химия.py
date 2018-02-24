print ('¬ведите вход€щие и полученные вещества в формате H2_(S-O4):')
A = input ().split ()
B = input ().split ()
A1 = []
B1 = []
for i in range (len (A)):
    A1.append (A [i].split ('_'))
for i in range (len (B)):
    B1.append (B [i].split ('_'))
print (A1, B1)
for i in range (len (A1)):
    j = 0
    while A1 [i][j].count ('(') == 0: j += 1
    if A1 [i][j].count ('(') > 0:
        s = A1 [i][j]
        x = s.find ('-')
        y = s.find (')')
        s1 = s [1:x]
        s2 = s [x + 1:y]
        if y + 1 == len (s): n = 1
        else: n = int (s [y + 1:len (s)])
        if len (s1) == 1: n1 = 1
        elif len (s1) > 2: n1 = int (s1 [2:len (s1)])
        elif s1 [1] == '1' or s1 [1] == '2' or s1 [1] == '3' or s1 [1] == '4' or s1 [1] == '5' or s1 [1] == '6' or s1 [1] == '7' or s1 [1] == '8' or s1 [1] == '9': n1 = int (s1 [1:len (s1)])
        else: n1 = 1
        if len (s2) == 1: n2 = 1
        elif len (s2) > 2: n2 = int (s2 [2:len (s2)])
        elif s2 [1] == '1' or s2 [1] == '2' or s2 [1] == '3' or s2 [1] == '4' or s2 [1] == '5' or s2 [1] == '6' or s2 [1] == '7' or s2 [1] == '8' or s2 [1] == '9': n2 = int (s2 [1:len (s2)])
        else: n2 = 1
        if n1 == 1: s1 = s1 [:len (s1) - len (str (n1)) + 1] + str (n1 * n)
        else: s1 = s1 [:len (s1) - len (str (n1))] + str (n1 * n)
        if n2 == 1: s2 = s2 [:len (s2) - len (str (n2)) + 1] + str (n2 * n)
        else: s2 = s2 [:len (s2) - len (str (n2))] + str (n2 * n)
        A1 [i][-1] = s1
        A1 [i].append (s2)
for i in range (len (B1)):
    j = 0
    while B1 [i][j].count ('(') == 0: j += 1
    if B1 [i][j].count ('(') > 0:
        s = B1 [i][j]
        x = s.find ('-')
        y = s.find (')')
        s1 = s [1:x]
        s2 = s [x + 1:y]
        if y + 1 == len (s): n = 1
        else: n = int (s [y + 1:len (s)])
        if len (s1) == 1: n1 = 1
        elif len (s1) > 2: n1 = int (s1 [2:len (s1)])
        elif s1 [1] == '1' or s1 [1] == '2' or s1 [1] == '3' or s1 [1] == '4' or s1 [1] == '5' or s1 [1] == '6' or s1 [1] == '7' or s1 [1] == '8' or s1 [1] == '9': n1 = int (s1 [1:len (s1)])
        else: n1 = 1
        if len (s2) == 1: n2 = 1
        elif len (s2) > 2: n2 = int (s2 [2:len (s2)])
        elif s2 [1] == '1' or s2 [1] == '2' or s2 [1] == '3' or s2 [1] == '4' or s2 [1] == '5' or s2 [1] == '6' or s2 [1] == '7' or s2 [1] == '8' or s2 [1] == '9': n2 = int (s2 [1:len (s2)])
        else: n2 = 1
        if n1 == 1: s1 = s1 [:len (s1) - len (str (n1)) + 1] + str (n1 * n)
        else: s1 = s1 [:len (s1) - len (str (n1))] + str (n1 * n)
        if n2 == 1: s2 = s2 [:len (s2) - len (str (n2)) + 1] + str (n2 * n)
        else: s2 = s2 [:len (s2) - len (str (n2))] + str (n2 * n)
        B1 [i][-1] = s1
        B1 [i].append (s2)
print (A1, B1)