import unittest

from linked_list import Node, LinkedList

class LinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.headValue = 1
        self.nValue = 2
        self.nnValue = 3
        self.l = LinkedList(self.headValue)

    def test_property(self):
        n = Node()
        n.value = 1
        self.assertEqual(n.value, 1, "Property test") 

    def test_linked_list_head_exist(self):
        self.assertTrue(isinstance(self.l.head, Node))

    def test_linked_list_append_next(self):
        self.l.append(self.nValue)
        self.assertEqual(self.l.head._next.value, self.nValue, "append node next")

    def test_linked_list_append_prev(self):
        self.l.append(self.nValue)
        self.assertEqual(self.l.head._next.prev.value, self.l.head.value, "append node prev")

    def test_linked_list_many_time_append_next(self):
        self.l.append(self.nValue)
        self.l.append(self.nnValue)
        self.assertEqual(self.l.head._next.value, self.nValue, "append many time next")

    def test_linked_list_many_time_append_prev(self):
        self.l.append(self.nValue)
        self.l.append(self.nnValue)
        self.assertEqual(self.l.head._next._next.prev.value, self.nValue, "append many time prev")

    def test_call(self):
        self.l.append(self.nValue)
        self.l.append(self.nnValue)
        self.assertEqual(self.l.call(2).value, self.nnValue, "check call(2)")
        self.assertEqual(self.l.call(1).value, self.nValue, "check call(1)")
        self.assertEqual(self.l.call(0).value, self.headValue, "check call(0)")

    def test_delete(self):
        self.l.append(self.nValue)
        self.l.append(self.nnValue)
        self.l.delete(1)
        self.assertEqual(self.l.head._next.value, self.nnValue, "check delete function next")
        self.assertEqual(self.l.head._next.prev.value, self.headValue, "check delete function prev")
    '''
    def test_delete_last_node(self):
        self.l.append(self.nValue)
        self.l.append(self.nnValue)
        self.l.delete(2)
        self.assertEqual(self.l.findLastNode().value, self.nValue, "delete last node")

    def test_delete_first_node(self):
        self.l.append(self.nValue)
        self.l.append(self.nnValue)
        self.l.delete(0)
        self.assertEqual(self.l.call(0), self.nValue, "delete first node")
   '''
if __name__ == "__main__":
    unittest.main()
