n = int (input ())
A = list (map (int, input ().split()))
k = int (input ())
mins = sum (A [0:k])
for i in range (0, n - k + 1):
    mins = min (mins, sum (A [i:i+k]))
print (mins)