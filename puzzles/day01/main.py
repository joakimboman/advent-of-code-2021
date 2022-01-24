from utils.file_reader import FileReader
import os


def part1(puzzle_input):
    previous = None
    increased_count = 0

    for i in puzzle_input:
        if previous and i > previous:
            increased_count += 1
        previous = i

    return increased_count


def part2(puzzle_input):
    previous_sum = None
    increased_count = 0

    for i in range(2, len(puzzle_input)):
        current_sum = puzzle_input[i - 2] + puzzle_input[i - 1] + puzzle_input[i]
        if previous_sum and current_sum > previous_sum:
            increased_count += 1
        previous_sum = current_sum

    return increased_count


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [int(x) for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
