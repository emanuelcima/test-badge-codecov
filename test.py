import unittest

from example import div, hello, perfom_hello, sum

class TestExample(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1,1), 2)