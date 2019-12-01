# --- Day 1: The Tyranny of the Rocket Equation ---
import math


def calculate_fuel(mass):
    return math.floor(mass/3) - 2


def calculate_fuel_4_real(mass, sum):
    fuel = calculate_fuel(mass)
    if fuel <= 0:
        return sum
    else:
        return calculate_fuel_4_real(fuel, sum + fuel)


def day1():
    sumPart1 = 0
    sumPart2 = 0
    with open('input-day1.txt') as file:
        for line in file:
            sumPart1 += calculate_fuel(int(line))
            sumPart2 += calculate_fuel_4_real(int(line), 0)
        print('Sum of fuel requirements part1:', sumPart1)
        print('Sum of fuel requirements part2:', sumPart2)


day1()
