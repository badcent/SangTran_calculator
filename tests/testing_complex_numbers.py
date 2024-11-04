import unittest
from calculator import complex_add, complex_divide, complex_multiply, complex_subtract

class TestComplexOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(complex_add(1+2j,3+4j), 4+6j)

    def test_subtract(self):
        self.assertEquals(complex_subtract(10j+1,5j), 0)

    def test_multiply(self):
            self.assertEquals(complex_multiply(10 + 11j, 100+1j), 989+1110j)

    def test_divide(self):
        self.assertEqual(complex_divide(25j + 10, 5j+5), 3.5+1.5j)

if __name__ == '__main__':
    unittest.main()