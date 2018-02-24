N = int (input ())
a = N // 48
b = (N - 48 * a) // 16
c = (N - a * 48 - b * 16) // 4
d = N - a * 48 - b * 16 - c * 4
print (a, b, c, d)