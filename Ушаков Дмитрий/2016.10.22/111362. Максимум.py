n, m = map (int, input().split())
A = []
for i in range (n):
    A.append (list (map (int, input ().split ())))
x = A [0][0]
k = 0
l = 0
for i in range (n):
    for j in range (m):
        if x < A [i][j]:
            k, l = i, j
            x = A [i][j]
print (k, l)