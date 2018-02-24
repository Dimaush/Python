import random
from datetime import datetime

c = 1000000

A = []
B = []
for i in range (c):
    A.append (random.randint (1, 100))
    B.append (random.randint (1, 100))

beforemultiply = datetime.now ()
for i in range (c):
    p = A [i] * B [i]
aftermultiply = datetime.now ()
print (aftermultiply - beforemultiply)

beforeadd = datetime.now ()
for i in range (c):
    s = A [i] < B [i]
afteradd = datetime.now ()
print (afteradd - beforeadd)