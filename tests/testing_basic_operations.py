import unittest
from calculator import add, subtract, multiply, divide

class TestBasicOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

    def test_subtract(self):
        self.assertEquals(subtract(100,10), 90)

    def test_multiply(self):
            self.assertEquals(multiply(5,5), 25)


    def test_divide(self):
        self.assertEqual(divide(10,2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide (10,0)

if __name__ == '__main__':
    unittest.main()

    