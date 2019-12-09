# --- Day 6: Universal Orbit Map ---

import os
import sys


class Node:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.ancestors = []

    def add_ancestor(self, ancestor):
        self.ancestors.append(ancestor)


def create_node_tree(orbits_list):
    tree = {}
    for orbits in orbits_list:
        (orbit_parent, orbit_child) = orbits.split(')')
        node = Node(orbit_child, orbit_parent)
        tree[orbit_child] = node
    return tree


def get_all_orbits(tree):
    all_ancestors = 0
    for key, node in tree.items():
        ancestors = 0
        if(node.parent != 'COM'):
            ancestors += 1
            node.add_ancestor(node.parent)
            tmp_parent = tree[node.parent]
            while True:
                if tmp_parent.parent == 'COM':
                    ancestors += 1
                    node.add_ancestor(tmp_parent.parent)
                    break
                tmp_parent = tree[tmp_parent.parent]
                ancestors += 1
                node.add_ancestor(tmp_parent.key)
        else:
            ancestors += 1
            node.add_ancestor(node.parent)
        all_ancestors += ancestors
    return (all_ancestors, tree)


def shortest_way_to_santa(tree):
    santa = tree['SAN'].ancestors
    me = tree['YOU'].ancestors
    first_common_node = get_first_common_node(santa, me)
    santa_length = santa.index(first_common_node)
    me_length = me.index(first_common_node)
    return santa_length + me_length


def get_first_common_node(list1, list2):
    result = None
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return x

    return result


def day6():
    with open(os.path.join(sys.path[0], "input_day6.txt")) as file:
        orbits = [line.rstrip() for line in file]
    (number_of_orbits, tree) = get_all_orbits(create_node_tree(orbits))
    print('Answer part1:', number_of_orbits)
    print('Answer part2:', shortest_way_to_santa(tree))


day6()
