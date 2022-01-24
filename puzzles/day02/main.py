from utils.file_reader import FileReader
import os
import re


def part1(puzzle_input):
    horizontal_position = depth = 0
    for i in puzzle_input:
        num = int(re.sub('[^0-9]', '', i))
        if 'up' in i:
            depth -= num
        elif 'down' in i:
            depth += num
        else:
            horizontal_position += num
    return horizontal_position * depth


def part2(puzzle_input):
    horizontal_position = depth = aim = 0
    for i in puzzle_input:
        num = int(re.sub('[^0-9]', '', i))
        if 'up' in i:
            aim -= num
        elif 'down' in i:
            aim += num
        else:
            horizontal_position += num
            depth += (num * aim)
    return horizontal_position * depth


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
