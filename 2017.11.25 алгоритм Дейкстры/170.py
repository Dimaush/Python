N = int (input ())
S, F = map (int, input ().split ())
S, F = S - 1, F - 1
R = int (input ())
D = []
T = []
for i in range (R):
    l, tl, r, tr = map (int, input ().split ())
    D.append ([l, r])
    T.append ([tl, tr])
print (D, T)

k = 10 ** 10
time = [k] * N
time [S] = 0
used = [False] * N
min_time = 0
min_vertex = S
while min_time < k:
    i = min_vertex
    used [i] = True
    for j in range (N):
        for w in range (R):
            if D [w] == [i, j] and T [w][0] <= min_time:
                time [j] = min (time [j], min_time + (T [w][1] - T [w][0]))
    min_time = k
    for j in range (N):
        if not used [j] and time [j] < min_time:
            min_time = time [j]
            min_vertex = j

print (time)
if time [F] == k: print (-1)
else: print (time [F])