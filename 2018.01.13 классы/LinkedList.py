class Node:
    #data = 0
    #next_ = None
    def __init__ (self, data, next_):
        self.data = data
        self.next_ = next_

class LinkedList:
    head = None
    def pushleft (self, data):
        n = Node (data, self.head)
        #n.data = data
        #n.next_ = self.head
        self.head = n
    def pushright (self, data):
        p = self.head
        if p == None: self.pushleft (data)
        else:
            while p.next_ != None: p = p.next_
            n = Node (data, None)
            #n.data = data
            p.next_ = n
    def popleft (self):
        l = LinkedList ()
        if self.head != None:
            n = self.head
            self.head = n.next_
            n.next_ = None
            print ("Deleted:", n.data)
        else: print ('Error: the list is empty.')
    def popright (self):
        if self.head != None:
            l = LinkedList ()
            p1 = self.head
            p2 = p1.next_
            if p2 == None: self.popleft ()
            else:
                while p2.next_ != None: p1, p2 = p2, p2.next_
                print ("Deleted:", p2.data)
                p2.data, p2.next_ = None, None
                p1.next_ = None
        else: print ('Error: the list is empty.')
    def print_ (self):
        l = LinkedList ()
        p = self.head
        while p != None:
            print (p.data, end = ' ')
            p = p.next_
        print ()
    def elem (self, k, func):
        t1 = self.head
        flag = 0
        if t1 == None:
            print ("Error: the list's length is not enough to", func, "the data.")
            flag = 1
            t2 = None
        else:
            t2 = t1.next_
            for i in range (k - 1):
                if t2 == None:
                    print ("Error: the list's length is not enough to", func, "the data.")
                    flag = 1
                    break
                else: t1, t2 = t1.next_, t2.next_
        return flag, t1, t2
    def insert (self, k, data):
        if k == 0: self.pushleft (data)
        else:
            flag, t1, t2 = self.elem (k, 'insert')
            if flag == 0:
                n = Node (data, t2)
                #n.data = data
                #n.next_ = t2
                t1.next_ = n
    def delete (self, k):
        if k == 0: self.popleft ()
        else:
            flag, t1, t2 = self.elem (k, 'delete')
            if flag == 0:
                if t2 != None:
                    print ("Deleted:", t2.data)
                    t1.next_ = t2.next_
                    t2.data = None
                    t2.next_ = None
                else: print ("Error: the list's length is not enough to delete the data.")
l = LinkedList()

print ()
print ("Hello! That's one-connected list simulator.")
print ("Commands:")
print ("1) pushleft [data]")
print ("2) pushright [data]")
print ("3) popleft")
print ("4) popright")
print ("5) insert [number] [data]")
print ("6) delete [number]")
print ("7) print")
print ("To end up please enter 'bye' (without quotes).")
print ()

r = list (map (str, input ().split ()))
while len (r) > 0 and r [0] != 'bye':
    if r [0] == 'pushleft': l.pushleft (r [1])
    elif r [0] == 'pushright': l.pushright (r [1])
    elif r [0] == 'popleft': l.popleft ()
    elif r [0] == 'popright': l.popright ()
    elif r [0] == 'print': l.print_ ()
    elif r [0] == 'insert': l.insert (int (r [1]), r [2])
    elif r [0] == 'delete': l.delete (int (r [1]))
    else: print ("Sorry, I can't understand you. Please try again.")
    r = list (map (str, input ().split ()))
print ("Bye!")