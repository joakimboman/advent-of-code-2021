import argparse
from puzzles.day01.main import run as day01
from puzzles.day02.main import run as day02
from puzzles.day03.main import run as day03
from puzzles.day04.main import run as day04
from puzzles.day05.main import run as day05
from puzzles.day06.main import run as day06
from puzzles.day07.main import run as day07
from puzzles.day08.main import run as day08
from puzzles.day09.main import run as day09
from puzzles.day10.main import run as day10
from puzzles.day11.main import run as day11
from puzzles.day12.main import run as day12
from puzzles.day13.main import run as day13
from puzzles.day14.main import run as day14
from puzzles.day15.main import run as day15
from puzzles.day16.main import run as day16
from puzzles.day17.main import run as day17
from puzzles.day18.main import run as day18


def default(_):
    print('No solution implemented!')


def main(puzzle_id):
    puzzles = {
        1: day01,
        2: day02,
        3: day03,
        4: day04,
        5: day05,
        6: day06,
        7: day07,
        8: day08,
        9: day09,
        10: day10,
        11: day11,
        12: day12,
        13: day13,
        14: day14,
        15: day15,
        16: day16,
        17: day17,
        18: day18,
        19: default,
        20: default,
        21: default,
        22: default,
        23: default,
        24: default,
        25: default,
    }
    print(f"--- DAY {puzzle_id} ---")
    for i in ['example', 'input']:
        print('')
        print(f"Puzzle {i}")
        puzzles[puzzle_id](i)
    print('')


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-p', '--puzzle', type=int, required=True, help='The puzzle id')
    ARGS = PARSER.parse_args()
    main(ARGS.puzzle)
