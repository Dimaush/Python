n, k = map (int, input ().split ())
P = list (map (int, input ().split ()))
K = [0] * (n - k + 1)
K [0] = sum (P [:k])
for i in range (1, len (K)):
    K [i] = K [i - 1] - P [i - 1] + P [k + i - 1]
K = [0] + K + [0]
ml = [K [0]]
mr = [K [-1]]
for i in range (1, len (K)):
    ml += [max (ml [-1], K [i])]
    mr = [max (mr [0], K [- i - 1])] + mr
M = []
for i in range (k, n - k + 1):
    M.append (max (ml [i - k], mr [i + k]))
M = set (M)
print (min (M))