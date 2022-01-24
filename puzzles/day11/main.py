import os
from utils.file_reader import FileReader


def increase_energy(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] < 10:
        matrix[row][col] += 1
        if matrix[row][col] > 9:
            for (i, j) in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row - 1, col - 1),
                           (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]:
                increase_energy(matrix, i, j)


def part1(puzzle_input):
    flashes = 0
    octopuses_matrix = []
    for line in puzzle_input:
        row = []
        for energy_level in line:
            row.append(int(energy_level))
        octopuses_matrix.append(row)
    for i in range(100):
        for row in range(len(octopuses_matrix)):
            for col in range(len(octopuses_matrix[0])):
                increase_energy(octopuses_matrix, row, col)
        for row in range(len(octopuses_matrix)):
            for col in range(len(octopuses_matrix[0])):
                if octopuses_matrix[row][col] == 10:
                    flashes += 1
                    octopuses_matrix[row][col] = 0
    return flashes


def part2(puzzle_input):
    octopuses_matrix = []
    for line in puzzle_input:
        row = []
        for energy_level in line:
            row.append(int(energy_level))
        octopuses_matrix.append(row)
    for i in range(100000):
        flashes = 0
        for row in range(len(octopuses_matrix)):
            for col in range(len(octopuses_matrix[0])):
                increase_energy(octopuses_matrix, row, col)
        for row in range(len(octopuses_matrix)):
            for col in range(len(octopuses_matrix[0])):
                if octopuses_matrix[row][col] == 10:
                    flashes += 1
                    octopuses_matrix[row][col] = 0
        if flashes == 100:
            return i + 1
    return None


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
