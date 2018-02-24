N = int (input ())
K = int (input ())
P = [0] * N
for i in range (K):
    x = 0
    m = 0
    s = 0
    for j in range (N):
        if P [j] == 0: x += 1
        else:
            if x > m:
                m = x
                s = j - x
            x = 0
    if x > m:
        m = x
        s = j + 1 - x
    P [s + m // 2] = 1
k = s + m // 2
l = 1
while k - l > -1 and P [k - l] == 0: l += 1
r = 1
while k + r < N and P [k + r] == 0: r += 1
print (min (l, r) - 1)
print (max (l, r) - 1)