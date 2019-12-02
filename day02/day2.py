# --- Day 2: 1202 Program Alarm ---

import os
import sys


def run_program(intcode, index=0):
    if(index >= len(intcode)):
        return intcode
    elif intcode[index] == 1:
        intcode[intcode[index+3]] = intcode[intcode[index + 1]] + \
            intcode[intcode[index+2]]
        return run_program(intcode, index + 4)
    elif intcode[index] == 2:
        intcode[intcode[index+3]] = intcode[intcode[index + 1]] * \
            intcode[intcode[index+2]]
        return run_program(intcode, index + 4)
    elif intcode[index] == 99:
        return intcode


def restore_and_run(noun, verb, intcode):
    intcode[1] = noun
    intcode[2] = verb
    return run_program(intcode)


def day2():
    with open(os.path.join(sys.path[0], "input_day2.txt")) as file:
        input = list(map(int, file.readline().split(',')))

        print('Answer part1:', restore_and_run(
            12, 2, input.copy())[0])

        for noun in range(0, 99):
            for verb in range(0, 99):
                proccessed_intcode = restore_and_run(
                    noun, verb, input.copy())[0]
                if(proccessed_intcode == 19690720):
                    print('Answer part2:', 100*noun+verb)
                    break


day2()
