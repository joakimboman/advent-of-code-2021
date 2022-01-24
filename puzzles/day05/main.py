import os
from utils.file_reader import FileReader


def larger_equal(x, y):
    return x >= y


def less_equal(x, y):
    return x <= y


def equal(x, y):
    return x == y


def part1(puzzle_input):
    hydrothermal_vents = {}
    for i in puzzle_input:
        coords = i.split(' -> ')
        coords_1 = coords[0].split(',')
        coords_2 = coords[1].split(',')
        x1 = int(coords_1[0])
        y1 = int(coords_1[1])
        x2 = int(coords_2[0])
        y2 = int(coords_2[1])

        conditional_func = less_equal
        increment = 1

        if y1 == y2:
            if x1 > x2:
                conditional_func = larger_equal
                increment = -1
            while conditional_func(x1, x2):
                if (x1, y1) in hydrothermal_vents:
                    hydrothermal_vents[(x1, y1)] += 1
                else:
                    hydrothermal_vents[(x1, y1)] = 1
                x1 += increment

        elif x1 == x2:
            if y1 > y2:
                conditional_func = larger_equal
                increment = -1
            while conditional_func(y1, y2):
                if (x1, y1) in hydrothermal_vents:
                    hydrothermal_vents[(x1, y1)] += 1
                else:
                    hydrothermal_vents[(x1, y1)] = 1
                y1 += increment

    more_than_two_lines_overlap = 0
    for _, value in hydrothermal_vents.items():
        if value >= 2:
            more_than_two_lines_overlap += 1

    return more_than_two_lines_overlap


def part2(puzzle_input):
    hydrothermal_vents = {}
    for i in puzzle_input:
        coords = i.split(' -> ')
        coords_1 = coords[0].split(',')
        coords_2 = coords[1].split(',')
        x1 = int(coords_1[0])
        y1 = int(coords_1[1])
        x2 = int(coords_2[0])
        y2 = int(coords_2[1])

        conditional_func_x = less_equal
        conditional_func_y = less_equal
        increment_x = 1
        increment_y = 1

        if x1 > x2:
            conditional_func_x = larger_equal
            increment_x = -1
        elif x1 == x2:
            conditional_func_x = equal
            increment_x = 0
        if y1 > y2:
            conditional_func_y = larger_equal
            increment_y = -1
        elif y1 == y2:
            conditional_func_y = equal
            increment_y = 0

        while conditional_func_x(x1, x2) and conditional_func_y(y1, y2):
            if (x1, y1) in hydrothermal_vents:
                hydrothermal_vents[(x1, y1)] += 1
            else:
                hydrothermal_vents[(x1, y1)] = 1
            x1 += increment_x
            y1 += increment_y

    more_than_two_lines_overlap = 0
    for _, value in hydrothermal_vents.items():
        if value >= 2:
            more_than_two_lines_overlap += 1

    return more_than_two_lines_overlap


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
