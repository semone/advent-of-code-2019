import unittest
from day3 import get_closest_intersection


class Day1Tests(unittest.TestCase):
    def test_get_closest_intersection(self):
        input = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
        input2 = ['R75,D30,R83,U83,L12,D49,R71,U7,L72',
                  'U62,R66,U55,R34,D71,R55,D58,R83']
        input3 = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                  'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']

        self.assertEqual(get_closest_intersection(input), (6, 30))
        self.assertEqual(get_closest_intersection(input2), (159, 610))
        self.assertEqual(get_closest_intersection(input3), (135, 410))


if __name__ == '__main__':
    unittest.main()
