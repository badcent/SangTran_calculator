import unittest
from calculator import power, sqrt, factorial

class TestAdvanceOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(power(2,3), 8)

    def test_subtract(self):
        self.assertEquals(sqrt(100), 10)

    def test_multiply(self):
            self.assertEquals(factorial(11), 39916800)

if __name__ == '__main__':
     unittest.main()