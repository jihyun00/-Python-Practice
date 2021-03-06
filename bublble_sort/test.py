import unittest

from bubble import swap, bubble

class MyBubbleSortTest(unittest.TestCase):
    def setUp(self):
       self.arr = [1, 9, 4, 7, 2, 3, 8, 6, 5, 10]
       self.a = 2
       self.b = 3

    def test_result(self):
        self.assertEqual(swap(2, 3), (3, 2)) 
       
    def test_bubble(self):
        self.assertEqual(, ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))

if __name__ == "__main__":
    unittest.main()
