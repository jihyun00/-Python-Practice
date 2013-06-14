import unittest

from newton import sq, enough

class MySqrtTestCase(unittest.TestCase):
    def setUp(self):
        self.n = 2

    def test_iter_sqrt4(self):
        self.assertTrue(enough(sq(2), 2), "Iter")

if __name__ == "__main__":
    unittest.main()
