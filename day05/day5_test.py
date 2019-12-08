import unittest
from day5 import parameter_mode, get_parameter


class Day5Tests(unittest.TestCase):
    def test_parameter_mode(self):
        self.assertEqual(parameter_mode(1), (1, 0, 0, 0))
        self.assertEqual(parameter_mode(1002), (2, 0, 1, 0))

    def test_get_value(self):
        self.assertEqual(get_parameter(0, [1002, 4, 3, 4, 33], 1), 33)
        self.assertEqual(get_parameter(1, [1002, 4, 3, 4, 33], 2),  3)


if __name__ == '__main__':
    unittest.main()
