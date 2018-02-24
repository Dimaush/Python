class Node:
    data = 0
    nextt = None
    def __init__(self, data):
        self.data = data 
class linkedlist:
    head = None
    def pushleft(self, data):
        n = Node(data)
        n.nextt = self.head
        self.head = n
    def popleft(self):
        z = self.head
        if z != None:
            self.head = z.nextt
            print(z.data)
            z.nextt = None
        else:
            print('empty!!!')
    def printt(self):
        m = self.head
        while m != None:
            print(m.data)
            m = m.nextt       
    def insert(self, n, q):
        flag = True
        if n == 0:
            self.pushleft(q)
        else:
            m = self.head
            for i in range(n - 1):
                if m == None or m.nextt == None:
                    return False    
                else:
                    m = m.nextt            
            if m != False:        
                f = m.nextt
                s = Node(q)
                s.nextt = f
                m.nextt = s
            else:
                print('list index out of range!!!')  
    def delete(self, n):
        flag = True
        m = self.head
        if m == None:
            print('empty!!!')
        elif n == 0:
            self.popleft()
        else:
            m = self.head
            for i in range(n - 1):
                if m.nextt == None:
                    return False    
                else:
                    m = m.nextt
            if m != False and m.nextt != None:
                k = m.nextt
                h = k.nextt
                m.nextt = h
            else:
                print('list index out of range!!!')      

l = linkedlist()
l.insert(0, 5)