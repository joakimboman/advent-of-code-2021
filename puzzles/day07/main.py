import os
import sys
from utils.file_reader import FileReader


def part1(puzzle_input):
    positions = [int(x) for x in puzzle_input[0].split(',')]
    max_position = max(positions)
    min_fuel_cost = sys.maxsize

    for i in range(max_position):
        fuel_cost = 0
        for p in positions:
            fuel_cost += abs(p - i)
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost

    return min_fuel_cost


def part2(puzzle_input):
    positions = [int(x) for x in puzzle_input[0].split(',')]
    max_position = max(positions)
    min_fuel_cost = sys.maxsize

    for i in range(max_position):
        fuel_cost = 0
        for p in positions:
            fuel_cost += int(abs(p - i) * (abs(p - i) + 1) / 2)
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost

    return min_fuel_cost


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
