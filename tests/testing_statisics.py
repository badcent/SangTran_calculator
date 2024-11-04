import unittest
from calculator import mean, median, mode, stdev 

class TestStatistics(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1,4,5,10]), 5)

    def test_median(self):
        self.assertEqual(median([5,4,3,2,1], 3))

    def test_mode(self):
        self.assertEqual(mode([10,4,2,9,4,6]), 4)

    def test_stdev(self):
        self.assertEqual(stdev([5,4,2,5,4]), 1.224744871391589)
        
if __name__ == '__main__':
    unittest.main()