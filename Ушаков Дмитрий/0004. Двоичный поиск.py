lena, lenk = map (int, input ().split ())
A = list (map (int, input ().split ()))
K = list (map (int, input ().split ()))
for i in range (len (K)):
    a = 0
    b = len (A) - 1
    while b - a > 1:
        m = (b + a) // 2
        if A [m] > K [i]: b = m
        else: a = m
    if A [a] == K [i]: flag = 'YES'
    elif A [b] == K [i]: flag = 'YES'
    else: flag = 'NO'
    print (flag)