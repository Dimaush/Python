H, M = map (int, input (). split ())
S1, S2, F1, F2 = map (int, input (). split ())
N = int (input ())
m = [0] * H * M
m[0] = 1
for i in range (N - 1):
    A = list(map (int, input (). split ()))
    m[(A[0] * M + A[1]) % (H * M)] += 1
print (m)
n = H * M - ((F1 - S1) * M + (F2 - S1))
k = 0
D = []
for i in range (len (m)):
    l = m[i:i + n]
    s = 0
    for j in range (len (l)):
        s += l[j]
    if s == 0:
        k += 1
        D.append (i)
if k > 0:
    print(D[0])
else:
    print ('Impossible')