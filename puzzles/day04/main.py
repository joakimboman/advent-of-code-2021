import os
import re
from utils.file_reader import FileReader


class BingoBoard:
    def __init__(self):
        self.board = []

    def update_board(self, val):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col][0] == val:
                    self.board[row][col] = (val, True)

    def is_bingo(self):
        rows = [0, 0, 0, 0, 0]
        cols = [0, 0, 0, 0, 0]
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col][1]:
                    rows[row] += 1
                    cols[col] += 1
        if 5 in rows or 5 in cols:
            return True
        return False

    def get_sum_of_unmarked(self):
        sum_unmarked = 0
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if not self.board[row][col][1]:
                    sum_unmarked += int(self.board[row][col][0])
        return sum_unmarked


def get_bingo_boards(puzzle_input):
    boards = []
    count = 0
    current_board = BingoBoard()
    for row in puzzle_input[1:]:
        if row == '':
            continue
        nums = re.split('\\s+', row)
        bingo_nums = [(x, False) for x in nums]
        current_board.board.append(bingo_nums)
        if count < 4:
            count += 1
        else:
            count = 0
            boards.append(current_board)
            current_board = BingoBoard()
    return boards


def part1(puzzle_input):
    boards = get_bingo_boards(puzzle_input)
    drawn_numbers = puzzle_input[0].split(',')
    score = None
    for num in drawn_numbers:
        for board in boards:
            board.update_board(num)
            if board.is_bingo():
                return int(num) * board.get_sum_of_unmarked()
    return score


def part2(puzzle_input):
    boards = get_bingo_boards(puzzle_input)
    drawn_numbers = puzzle_input[0].split(',')
    score = None
    boards_with_bingo = [False for _ in boards]
    for num in drawn_numbers:
        for i, board in enumerate(boards):
            board.update_board(num)
            if boards_with_bingo[i] or board.is_bingo():
                boards_with_bingo[i] = True
                if False not in boards_with_bingo:
                    return int(num) * board.get_sum_of_unmarked()
    return score


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip().lstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
