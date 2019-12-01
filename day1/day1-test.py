import unittest
from day1 import calculate_fuel, calculate_fuel_4_real


class Day1Tests(unittest.TestCase):
    def test_calculate_fuel(self):
        self.assertEqual(calculate_fuel(12), 2)
        self.assertEqual(calculate_fuel(14), 2)
        self.assertEqual(calculate_fuel(1969), 654)
        self.assertEqual(calculate_fuel(100756), 33583)

    def test_calculate_fuel_4_real(self):
        self.assertEqual(calculate_fuel_4_real(1969, 0), 966)
        self.assertEqual(calculate_fuel_4_real(100756, 0), 50346)


if __name__ == '__main__':
    unittest.main()
