import os
import sys


def get_closest_intersection(wires):
    grid1 = get_grid(wires[0])
    grid2 = get_grid(wires[1])
    intersections = set(grid1).intersection(grid2)
    distances = list(map(manhattan_distance, intersections))

    stepsList = []
    for i in intersections:
        steps1 = grid1.index(i)
        steps2 = grid2.index(i)
        if(sum:= steps1 + steps2) > 0:
            stepsList.append(sum)

    return (min(i for i in distances if i > 0), min(i for i in stepsList if i > 0))


def manhattan_distance(coord):
    return abs(0-coord[1]) + abs(0-coord[0])


def get_grid(wire):
    position = (0, 0)
    positions = [position]
    directions = {'R': (1, 0), 'D': (
        0, -1), 'U': (0, 1), 'L': (-1, 0)}

    for values in wire.split(','):
        direction = directions.get(values[0])
        stop = int(values[1:])
        i = 1
        while i <= stop:
            positions.append((position[0] + direction[0] * i,
                              position[1] + direction[1] * i))
            i += 1
        position = (position[0] + direction[0] * stop,
                    position[1] + direction[1] * stop)
    return positions


def day3():
    with open(os.path.join(sys.path[0], "input_day3.txt")) as file:
        input = file.readlines()
        print('Answer: ', get_closest_intersection(input))


day3()
