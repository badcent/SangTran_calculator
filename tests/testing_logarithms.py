import unittest
from calculator import log, ln, exp

class TestLogarithms(unittest.TestCase):
    def test_log(self):
        self.assertEqual(log(25), 0.3010299956639812) 

    def test_ln(self):
        self.assertEqual(ln(25), 3.2188758248682006)

    def test_exp(self):
        self.assertEqual(exp(5,5), 3125)

if __name__ == '__main__':
    unittest.main()