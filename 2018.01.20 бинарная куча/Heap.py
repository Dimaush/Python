import math

def height (heap):
    return math.ceil (math.log2 (len (heap) + 1))

def change (M, x, y):
    M [x], M [y] = M [y], M [x]
    return M

def heapify (heap, k):
    flag = max (2 - len (heap), 0)
    while flag == 0:
        if len (heap) == 2 * k + 2:
            if heap [k] < heap [2 * k + 1]: heap, k = change (heap, k, 2 * k + 1), 2 * k + 1
            else: flag = 1
        else:
            if heap [k] < heap [2 * k + 1] or heap [k] < heap [2 * k + 2]:
                if heap [2 * k + 1] >= heap [2 * k + 2]: heap, k = change (heap, k, 2 * k + 1), 2 * k + 1
                else: heap, k = change (heap, k, 2 * k + 2), 2 * k + 2
            else: flag = 1
        if len (heap) <= 2 * k + 1: flag = 1
    return heap

def add (heap, data):
    heap.append (data)
    i = len (heap) - 1
    while i > 0 and heap [(i - 1) // 2] < heap [i]:
        heap [i], heap [(i - 1) // 2] = heap [(i - 1) // 2], heap [i]
        i = (i - 1) // 2
    return heap

def popmax (heap):
    if len (heap) == 0: print ("Error: the list is empty.")
    else:
        heap [0], heap [-1] = heap [-1], heap [0]
        a = heap.pop (-1)
        print ("Deleted:", a)
        return heapify (heap, 0)

def print_ (heap):
    #print (heap)
    h = height (heap)
    d = 0
    for i in range (h):
        for j in range (min (2 ** i, len (heap) - d)):
            print (heap [d], end = ' ')
            d += 1
        print ()

heap = []

print ()
print ("Hello! That's binary heap simulator.")
print ("Commands:")
print ("1) add [data]")
print ("2) popmax")
print ("3) print")
print ("To end up please enter 'bye' without quotes.")
print ()

r = list (map (str, input ().split ()))
while len (r) > 0 and r [0] != 'bye':
    if r [0] == 'add': heap = add (heap, int (r [1]))
    elif r [0] == 'popmax': heap = popmax (heap)
    elif r [0] == 'print': print_ (heap)
    else: print ("Sorry, I can't understand you. Please try again.")
    r = list (map (str, input ().split ()))
print ("Bye!")