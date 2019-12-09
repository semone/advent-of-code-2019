import unittest
from day6 import get_all_orbits, create_node_tree, shortest_way_to_santa

input1 = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F',
          'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
input2 = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F',
          'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']


class Day6Tests(unittest.TestCase):
    def test_get_all_orbits(self):
        self.assertEqual(get_all_orbits(create_node_tree(input1))[0], 42)

    def test_get_closest(self):
        self.assertEqual(shortest_way_to_santa(
            get_all_orbits(create_node_tree(input2))[1]), 4)


if __name__ == '__main__':
    unittest.main()
