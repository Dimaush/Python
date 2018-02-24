from heapq import heappush, heappop

N = int (input ())
heap = []
data = list (map (int, input ().split ()))
for item in data: heappush (heap, item)
ordered = []
while heap: ordered.append (heappop (heap))
data . sort ()
data == ordered
print (* data)