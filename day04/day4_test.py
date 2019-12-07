import unittest
from day4 import has_adjacent, does_not_decrease, remove_larger_groups


class Day4Tests(unittest.TestCase):
    def test_has_adjasent(self):
        # self.assertEqual(has_adjacent("112233"), True)
        self.assertEqual(remove_larger_groups("123444"), '123')
        self.assertEqual(remove_larger_groups("111111"), '')
        self.assertEqual(remove_larger_groups("111222"), '')
        self.assertEqual(remove_larger_groups("112233"), '112233')

    def test_has_adjasent_part1(self):
        self.assertEqual(has_adjacent("122344"), True)
        self.assertEqual(has_adjacent("223450"), True)
        self.assertEqual(has_adjacent("111111"), True)
        self.assertEqual(has_adjacent("123789"), False)

    def test_does_not_decrease(self):
        self.assertEqual(does_not_decrease("223450"), False)
        self.assertEqual(does_not_decrease("123789"), True)
        self.assertEqual(does_not_decrease("111111"), True)


if __name__ == '__main__':
    unittest.main()
