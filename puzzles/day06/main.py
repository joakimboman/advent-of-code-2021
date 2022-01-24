import os
from utils.file_reader import FileReader


def solution(puzzle_input, iterations):
    fish = puzzle_input[0].split(',')
    timer = dict.fromkeys(range(9), 0)
    for f in fish:
        timer[int(f)] += 1
    for _ in range(iterations):
        num_new_fish = timer[0]
        previous_timer = timer[0]
        for i in range(6, -1, -1):
            tmp = timer[i]
            timer[i] = previous_timer
            previous_timer = tmp
        timer[6] += timer[7]
        timer[7] = timer[8]
        timer[8] = num_new_fish
    return sum(timer.values())


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {solution(puzzle_input, 80)}")
    print(f"Part 2: {solution(puzzle_input, 256)}")
