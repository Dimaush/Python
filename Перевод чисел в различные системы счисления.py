print ('������� ������� ���������, �� ������� �� ������ ��������� �����:', end = ' ')
g = int (input ())
print ('������� ����� � � ����� ������� ���������:', end = ' ')
N = int (input ())
print ('�������, � ����� ������� ��������� �� ������ ��� ���������:', end = ' ')
n = int (input ())
a = 1
k = 0
x = 0
A = []
s = ''
p = 0
#for k in range (len (str (N))):
    #if int (str (N)) >= g:
        #s = s + '0'
    #else:
        #s = s + '1'
#h = s.find ('0')
#print (h)
for j in range (len (str (N))):
    p += int (str (N) [- j - 1]) * g ** j
while a < p + 1:
    a = a * n
    k += 1
a = a // n
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range (k):
    x = p % n
    #if x == 10:
        #x = 'A'
    #if x == 11:
        #x = 'B'
    #if x == 12:
        #x = 'C'
    #if x == 13:
        #x = 'D'
    #if x == 14:
        #x = 'E'
    #if x == 15:
        #x = 'F'
    if x >= 10: A.append (ALPHABET [x - 10])
    else: A.append (x)
    p = p // n
B = A [::-1]
print ('������� ����� �����', end = ' ')
for j in range (len (B)):
    print (B [j], end = '')
print ('.')