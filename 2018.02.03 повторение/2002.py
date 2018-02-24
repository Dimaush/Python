def func (q, dist, cy, cx, arrow):
    global ARR
    arrow1 = (arrow + 1) % 4
    sy, sx = cy + ARR [arrow][0], cx + ARR [arrow][1]
    ry, rx = cy + ARR [arrow1][0], cx + ARR [arrow1][1]
    if A [sy][sx] == ' ':
        dist [sy][sx] = min (dist [sy][sx], dist [cy][cx] + 1)
        q.append ([sy, sx, arrow])
    if A [ry][rx] == ' ':
        dist [ry][rx] = min (dist [ry][rx], dist [cy][cx] + 1)
        q.append ([ry, rx, arrow1])
    return q, dist

r, c = map (int, input ().split ())
A = []
for i in range (r):
    l = input ()
    L = []
    for j in range (len (l)):
        if l [j] == 'S': y0, x0 = i, j
        elif l [j] == 'F': y1, x1 = i, j
        L.append (l [j])
    A.append (L)

print (y0, x0)
print (y1, x1)
for i in range (r): print (* A [i])

INF = 10 ** 9
ARR = [[-1, 0], [0, 1], [1, 0], [0, -1]]

dist0 = [0] * r
for i in range (r): dist0 [i] = [INF] * c
dist0 [y0][x0] = 0
dist1 = [0] * r
for i in range (r): dist1 [i] = [INF] * c
dist1 [y0][x0] = 0
dist2 = [0] * r
for i in range (r): dist2 [i] = [INF] * c
dist2 [y0][x0] = 0
dist3 = [0] * r
for i in range (r): dist3 [i] = [INF] * c
dist3 [y0][x0] = 0

q0 = [[y0, x0, 0]]
q1 = [[y0, x0, 1]]
q2 = [[y0, x0, 2]]
q3 = [[y0, x0, 3]]

flag = 0
while flag == 0:
    if q0:
        h = q0.pop (0)
        q0, dist0 = func (q0, dist0, h [0], h [1], h [2])
    if q1:
        h = q1.pop (0)
        q1, dist1 = func (q1, dist1, h [0], h [1], h [2])
    if q2:
        h = q2.pop (0)
        q2, dist2 = func (q2, dist2, h [0], h [1], h [2])
    if q3:
        h = q3.pop (0)
        q3, dist3 = func (q3, dist3, h [0], h [1], h [2])
    
    #for i in range (r): print (* dist0 [i])
    #print ()
    for i in range (r): print (* dist1 [i])
    print ()
    #for i in range (r): print (* dist2 [i])
    #print ()
    #for i in range (r): print (* dist3 [i])
    #print ()
    u = input ()
print (dist [y1][x1])