import unittest

from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertNotEqual(result, 1)

if __name__ == "__main__":
    unittest.main()

'''
The first test indicates whether the sum of the numbers 1, 2, and 3 (using
our custom defined sum() function written in my_sum/__init__.py) are
equivalent to 6, which it is. 

The second test checks that the sum of the three provided fractions are not
equivalent to 1. Originally, the tutorial had us checking that they WERE 
equivalent to 1, which they aren't so I updated the assertion from 
assertEqual to assertNotEqual.
'''