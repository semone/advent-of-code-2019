# --- Day 5: Sunny with a Chance of Asteroids ---

import os
import sys


def execute(intcode, index, input):
    (code, mode1, mode2, mode3) = parameter_mode(intcode[index])

    if code == 99:
        return
    elif code == 1:
        parameter1 = get_parameter(mode1, intcode, index+1)
        parameter2 = get_parameter(mode2, intcode, index+2)
        intcode[intcode[index+3]] = parameter1 + parameter2
        return execute(intcode, index + 4, input)
    elif code == 2:
        parameter1 = get_parameter(mode1, intcode, index+1)
        parameter2 = get_parameter(mode2, intcode, index+2)
        intcode[intcode[index+3]] = parameter1 * parameter2
        return execute(intcode, index + 4, input)
    elif code == 3:
        intcode[intcode[index + 1]] = input
        return execute(intcode, index + 2, input)
    elif code == 4:
        parameter1 = get_parameter(mode1, intcode, index+1)
        output = parameter1
        return parameter1 if output != 0 else execute(intcode, index + 2, input)
    elif code == 5:
        parameter1 = get_parameter(mode1, intcode, index+1)
        parameter2 = get_parameter(mode2, intcode, index+2)
        index = parameter2 if parameter1 != 0 else index + 3
        return execute(intcode, index, input)
    elif code == 6:
        parameter1 = get_parameter(mode1, intcode, index+1)
        parameter2 = get_parameter(mode2, intcode, index+2)
        index = parameter2 if parameter1 == 0 else index + 3
        return execute(intcode, index, input)
    elif code == 7:
        parameter1 = get_parameter(mode1, intcode, index+1)
        parameter2 = get_parameter(mode2, intcode, index+2)

        intcode[intcode[index+3]] = 1 if parameter1 < parameter2 else 0
        return execute(intcode, index + 4, input)

    elif code == 8:
        parameter1 = get_parameter(mode1, intcode, index+1)
        parameter2 = get_parameter(mode2, intcode, index+2)

        intcode[intcode[index+3]] = 1 if parameter1 == parameter2 else 0
        return execute(intcode, index + 4, input)
    else:
        return  # stuff broke


def get_parameter(mode, intcode, index):
    return intcode[index] if mode else intcode[intcode[index]]


def parameter_mode(mode):
    full_parameters = str(mode).zfill(5)
    code = full_parameters[3:]
    modes = list(full_parameters[:3])
    return (int(code), int(modes[2]), int(modes[1]), int(modes[0]))


def day5():
    with open(os.path.join(sys.path[0], "input_day5.txt")) as file:
        input = list(map(int, file.readline().split(',')))
        print('Answer part1:', execute(input.copy(), 0, 1))
        print('Answer part2:', execute(input.copy(), 0, 5))


day5()
