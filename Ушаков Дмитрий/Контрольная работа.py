N = int(input())
K = int(input())
x = int(input())
y = int(input())
p = (2 * x + y) % K
if p == 0:
    p = K
