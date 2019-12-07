# --- Day 4: Secure Container ---
import re
import functools


def remove_larger_groups(input):
    # Find indices for larger groups
    iter = re.finditer(r"(\w)\1{2,5}", input)
    indices = [(m.start(0), m.end(0)) for m in iter]

    # no matches for larger inputs
    if len(indices) == 0:
        return input

    # merge if 3+3 not so nicew but...
    if len(indices) > 1:
        indices = [(indices[0][0], indices[1][1])]

    # remove groups from string
    return input[:int(indices[0][0])] + input[int(indices[0][1]):]


def has_adjacent(input):
    return False if re.search(r"(\w)\1", input) == None else True


def does_not_decrease(input):
    i = 0
    input_list = list(input)
    while i < len(input_list) - 1:
        if input_list[i] > input_list[i+1]:
            return False
        i += 1
    return True


def day4():
    max = 746325
    min = 264360
    part1 = 0
    part2 = 0
    for number in range(min, max):
        if not does_not_decrease(str(number)):
            continue
        if has_adjacent(str(number)):
            part1 += 1
        if has_adjacent(remove_larger_groups(str(number))):
            part2 += 1
    print('Answer part1:', part1)
    print('Answer part2:', part2)


day4()
