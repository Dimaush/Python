A = list (map (int, input ().split ()))
B = list (map (int, input ().split ()))
i = 0
j = 0
for k in range (len (A) + len (B)):
    if i == len (A):
        print (B [j], end = ' ')
        j += 1
    elif j == len (B):
        print (A [i], end = ' ')
        i += 1
    else:
        if A [i] < B [j]:
            print (A [i], end = ' ')
            i += 1
        else:
            print (B [j], end = ' ')
            j += 1