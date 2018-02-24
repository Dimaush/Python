l = input ()
n = len (l)
S = []
O = '([{'
C = ')]}'
ans = 'yes'
for i in range (n):
    x = l [i]
    if x in O: S.append (x)
    elif len (S) > 0 and O.find (S [-1]) == C.find (x): k = S.pop (-1)
    else:
        ans = 'no'
        break
if len (S) > 0: ans = 'no'
print (ans)