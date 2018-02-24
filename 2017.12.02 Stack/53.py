N = int (input ())
A = []
for i in range (N): A.append (list (map (int, input ().split ())))
P = []
if N == 2:
    s1, s2 = '', ''
    for i in range (A [0][0]): s1 += str (A [0][i + 1])
    for i in range (A [1][0]): s2 += str (A [1][- i - 1])
    s = s1 + s2
    #print (s)
    x, y = s.find ('2'), s.rfind ('1')
    #print (x, y)
    if x != -1 and y != -1 and x - y != 1: print (0)
    else:
        if x < A [0][0]:
            for i in range (A [0][0] - x): print (1, 2)
        elif y >= A [0][0]:
            for i in range (y - A [0][0] + 1): print (2, 1)
    
else:
    for i in range (1, N):
        for j in range (A [i][0]):
            x = A [i].pop (-1)
            A [i][0] -= 1
            A [0].append (x)
            A [0][0] += 1
            print (i + 1, 1)
    #print (A)
    L = A [0][0]
    for i in range (L):
        x = A [0].pop (-1)
        A [0][0] -= 1
        if x == 1:
            A [1].append (x)
            A [1][0] += 1
            print (1, 2)
        else:
            A [x - 1].append (x)
            A [x - 1][0] += 1
            print (1, x)
    for i in range (A [1][0]):
        x = A [1].pop (-1)
        A [1][0] -= 1
        if x == 1:
            A [0].append (x)
            A [0][0] += 1
            print (2, 1)
        else:
            A [2].append (x)
            A [2][0] += 1
            print (2, 3)
    flag = 1
    while flag == 1:
        if A [2][-1] == 3: flag = 0
        else:
            x = A [2].pop (-1)
            A [2][0] -= 1
            A [1].append (x)
            A [1][0] += 1
            print (3, 2)
    #print (A)