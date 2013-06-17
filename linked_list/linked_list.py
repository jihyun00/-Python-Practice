class Node(object):
    def __init__(self):
        self.data = None
        self._next = None
        self.prev = None

    @property
    def value(self):
        return self.data

    @value.setter
    def value(self, d):
        self.data = d

class LinkedList(object):
    def __init__(self, v):
        self._head = Node()
        self._head.value = v

    @property
    def head(self):
        return self._head

    def append(self, v):
        newNode = Node()
        newNode.value = v
        lastNode = self.findLastNode()
        lastNode._next = newNode
        newNode.prev = lastNode

    def findLastNode(self):
        n = self._head
        while n._next is not None:
            n = n._next
        return n

    def call(self, n):
        m = self._head
        for i in xrange(n):
            m = m._next
            
        return m
            
            
