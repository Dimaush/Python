N = int (input ())
A = int (input ())
B = int (input ())
C = int (input ())
D = int (input ())
x = A / B
y = C / D
m1 = ((N + A - 1) // A) * B
m2 = ((N + C - 1) // C) * D
m3 = N

#if x > y:
m4 = (N // A) * B + (((N - (N // A) * A) + C - 1) // C) * D
m5 = (N // A) * B + (N - (N // A) * A)
m6 = (N // A) * B + ((N - (N // A) * A) // C) * D + (N - (N // A) * A - ((N - (N // A) * A) // C) * C)
#else:
m7 = (N // C) * D + (((N - (N // C) * C) + A - 1) // A) * B
m8 = (N // C) * D + (N - (N // C) * C)
m9 = (N // C) * D + ((N - (N // C) * C) // A) * B + (N - (N // C) * C - ((N - (N // C) * C) // A) * A)
#print (m1, m2, m3, m4, m5, m6)
print (min (m1, m2, m3, m4, m5, m6, m7, m8, m9))