A = []
protokol = []
enter = input ()
while enter != 'exit':
    p = enter [1]
    if p == 'u':
        x = enter [5:]
        A += x
        protokol.append ('ok')
    elif p == 'o':
        if len (A) > 0:
            x = A.pop (0)
            protokol.append (x)
        else: protokol.append ('error')
    elif p == 'r':
        if len (A) > 0: protokol.append (A [0])
        else: protokol.append ('error')
    elif p == 'i': protokol.append (len (A))
    elif p == 'l':
        A = []
        protokol.append ('ok')
    enter = input ()
protokol.append ('bye')

for i in range (len (protokol)): print (protokol [i])