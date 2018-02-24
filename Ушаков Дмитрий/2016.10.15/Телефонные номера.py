n = input ()
a = input ()
b = input ()
c = input ()

a = a.split ('-')
b = b.split ('-')
c = c.split ('-')
n = n.split ('-')

n1 = ''
a1 = ''
b1 = ''
c1 = ''

for i in range (len (a)):
    a1 += a[i]
for i in range (len (b)):
    b1 += b[i]
for i in range (len (c)):
    c1 += c[i]
for i in range (len (n)):
    n1 += n[i]

a1 = a1.split ('(')
b1 = b1.split ('(')
c1 = c1.split ('(')
n1 = n1.split ('(')

n2 = ''
a2 = ''
b2 = ''
c2 = ''

for i in range (len (a1)):
    a2 += a1[i]
for i in range (len (b1)):
    b2 += b1[i]
for i in range (len (c1)):
    c2 += c1[i]
for i in range (len (n1)):
    n2 += n1[i]

a2 = a2.split (')')
b2 = b2.split (')')
c2 = c2.split (')')
n2 = n2.split (')')

n3 = ''
a3 = ''
b3 = ''
c3 = ''

for i in range (len (a2)):
    a3 += a2[i]
for i in range (len (b2)):
    b3 += b2[i]
for i in range (len (c2)):
    c3 += c2[i]
for i in range (len (n2)):
    n3 += n2[i]

if len (a3) == 7:
    a3 = '495' + a3
if len (b3) == 7:
    b3 = '495' + b3
if len (c3) == 7:
    c3 = '495' + c3
if len (n3) == 7:
    n3 = '495' + n3

if len (a3) == 12:
    a3 = '8' + a3 [2:len (a3)]
if len (b3) == 12:
    b3 = '8' + b3 [2:len (b3)]
if len (c3) == 12:
    c3 = '8' + c3 [2:len (c3)]
if len (n3) == 12:
    n3 = '8' + n3 [2:len (n3)]

if len (a3) == 10:
    a3 = '8' + a3
if len (b3) == 10:
    b3 = '8' + b3
if len (c3) == 10:
    c3 = '8' + c3
if len (n3) == 10:
    n3 = '8' + n3

if n3 == a3: print ('YES')
else: print ('NO')
if n3 == b3: print ('YES')
else: print ('NO')
if n3 == c3: print ('YES')
else: print ('NO')