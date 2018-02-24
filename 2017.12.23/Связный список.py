class Node:
    def a (self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
 
    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'
 
    def clear(self):
        self.__init__()
 
#создание связного списка из 3-х элементов
L = LinkedList()
L.add(1)
L.add(2)
L.add(3)