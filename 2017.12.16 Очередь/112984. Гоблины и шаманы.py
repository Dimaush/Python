from collections import deque

N = int (input ())
P, Q = deque (), deque ()
for i in range (N):
    s = input ()
    if s [0] == '-':
        x = P.popleft ()
        print (x)
        if len (P) < len (Q):
            c = Q.popleft ()
            P.append (c)
    elif s [0] == '+':
        g = int (s [2:])
        Q.append (g)
        if len (P) < len (Q):
            c = Q.popleft ()
            P.append (c)
    else:
        g = int (s [2:])
        P.append (g)
        if len (P) - len (Q) > 1:
            c = P.pop ()
            Q.appendleft (c)