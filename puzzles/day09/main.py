import numpy as np
import os
from utils.file_reader import FileReader


def part1(puzzle_input):
    matrix = []
    num_rows = len(puzzle_input)
    for line in puzzle_input:
        row = []
        for number in line:
            row.append(int(number))
        matrix.append(row)
    num_cols = len(matrix[0])
    low_points = []
    for i in range(num_rows):
        for j in range(num_cols):
            current = matrix[i][j]
            if ((i - 1 < 0 or current < matrix[i - 1][j])
                    and (j - 1 < 0 or current < matrix[i][j - 1])
                    and (i + 1 >= num_rows or current < matrix[i + 1][j])
                    and (j + 1 >= num_cols or current < matrix[i][j + 1])):
                low_points.append(matrix[i][j])

    return sum(low_points) + len(low_points)


def part2(puzzle_input):
    matrix = []
    num_rows = len(puzzle_input)
    for line in puzzle_input:
        row = []
        for number in line:
            row.append(int(number))
        matrix.append(row)
    num_cols = len(matrix[0])
    basins = []
    for i in range(num_rows):
        for j in range(num_cols):
            current = matrix[i][j]
            if ((i - 1 < 0 or current < matrix[i - 1][j])
                    and (j - 1 < 0 or current < matrix[i][j - 1])
                    and (i + 1 >= num_rows or current < matrix[i + 1][j])
                    and (j + 1 >= num_cols or current < matrix[i][j + 1])):
                visited = []
                queue = []
                visited.append((i, j))
                queue.append((i, j))
                basin_size = 0
                while queue:
                    (x, y) = queue.pop(0)
                    if x < 0 or y < 0 or x >= num_rows or y >= num_cols or matrix[x][y] == 9:
                        continue
                    basin_size += 1
                    for neighbour in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                        if neighbour not in visited:
                            visited.append(neighbour)
                            queue.append(neighbour)
                basins.append(basin_size)

    return np.prod(np.array(sorted(basins)[-3:]))


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
