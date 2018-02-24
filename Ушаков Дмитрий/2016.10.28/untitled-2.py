A = list (map (int, input ().split()))
k = int (input ())
mins = sum (A [0:k])
S = mins
for i in range (0, len (A)):
    #print (S)
    S = S + A [(i + k) % len (A)] - A [i % len (A)]
    mins = min (mins, S)
print (mins)