import unittest
from calculator import sine, cosine, tangent

class TestTrig(unittest.TestCase):
    def test_sine(self):
        self.assertEqual(sine(180), 0.8939966636005579)


    def test_cosine(self):
        self.assertEqual(cosine(12), 0.8438539587324921)

    
    def test_tangent(self):
        self.assertEqual(tangent(1000), 1.4703241557027185)

if __name__ == '__main__':
    unittest.main()