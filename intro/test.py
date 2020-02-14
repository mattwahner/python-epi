
import p1
import unittest

class Test1(unittest.TestCase):

    def test_example(self):
        h = p1.h_index([1, 4, 1, 4, 2, 1, 3, 5, 6])
        self.assertEqual(h, 4)

