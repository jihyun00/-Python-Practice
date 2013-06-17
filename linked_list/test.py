import unittest

from linked_list import Node

class LinkedListTestCase(unittest.TestCase):
    def test_property(self):
        n = Node()
        n.value = 1
        self.assertEqual(n.value, 1, "Property test") 
       
if __name__ == "__main__":
    unittest.main()
