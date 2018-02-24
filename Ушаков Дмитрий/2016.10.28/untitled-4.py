A = list (map (int, input ().split()))
for k in range (1, len (A) + 1):
    mins = sum (A [0:k])
    S = mins
    s = [S]
    for i in range (0, len (A)):
        S = S + A [(i + k) % len (A)] - A [i % len (A)]
        s.append (S)
        mins = min (mins, S)
    s = s[0:len(s) - 1]
    f = 0
    for i in range (len (s)):
        if s[i] == 0:
            f = 1
    if f == 1:
        l = k
print (l)