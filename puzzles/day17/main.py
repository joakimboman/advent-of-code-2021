import os
import re
from utils.file_reader import FileReader


def part1(puzzle_input):
    target_area_start_y = int(re.match('.*y=(-?\\d+)\\..*', puzzle_input[0]).group(1))
    return int(target_area_start_y * (target_area_start_y + 1) / 2)


def check_if_target_is_hit(x_vel, y_vel, target_area_start_x, target_area_end_x, target_area_start_y,
                           target_area_end_y):
    x_position = 0
    y_position = 0
    while True:
        if target_area_start_x <= x_position <= target_area_end_x and \
                target_area_start_y <= y_position <= target_area_end_y:
            return True

        if x_position > target_area_end_x:
            return False

        if y_position < target_area_start_y:
            return False

        y_position += y_vel
        y_vel -= 1

        if x_vel != 0:
            x_position += x_vel
            x_vel -= 1

    return False


def part2(puzzle_input):
    coordinates = re.match('target area: x=(-?\\d+)\\.\\.(-?\\d+), y=(-?\\d+)\\.\\.(-?\\d+)', puzzle_input[0])
    target_area_start_x = int(coordinates.group(1))
    target_area_end_x = int(coordinates.group(2))
    target_area_start_y = int(coordinates.group(3))
    target_area_end_y = int(coordinates.group(4))

    velocity_values_meeting_criteria = set()
    max_y_vel = int(target_area_start_y * (target_area_start_y + 1) / 2)
    for x_vel in range(target_area_end_x + 1):
        y_vel = target_area_start_y
        while True:

            if y_vel > max_y_vel:
                break

            hit_target = check_if_target_is_hit(x_vel, y_vel, target_area_start_x, target_area_end_x,
                                                target_area_start_y, target_area_end_y)
            if hit_target:
                velocity_values_meeting_criteria.add((x_vel, y_vel))

            y_vel += 1

    return len(velocity_values_meeting_criteria)


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
