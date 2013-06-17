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
