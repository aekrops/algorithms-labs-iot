import unittest
import os
from lab4.algorithm import check_results

test1_in = os.path.join(os.path.dirname(__file__), 'data/ijones1.in')
test1_out = os.path.join(os.path.dirname(__file__), 'data/ijones1.out')
test2_in = os.path.join(os.path.dirname(__file__), 'data/ijones2.in')
test2_out = os.path.join(os.path.dirname(__file__), 'data/ijones2.out')
test3_in = os.path.join(os.path.dirname(__file__), 'data/ijones3.in')
test3_out = os.path.join(os.path.dirname(__file__), 'data/ijones3.out')


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, check_results(test1_in, test1_out))
        self.assertEqual(True, check_results(test2_in, test2_out))
        self.assertEqual(True, check_results(test3_in, test3_out))


if __name__ == '__main__':
    unittest.main()
