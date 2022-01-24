import os
from utils.file_reader import FileReader


def part1(puzzle_input):
    coordinates = set()
    folds = []
    for line in puzzle_input:
        if line == '':
            continue
        elif 'fold along' in line:
            folds.append(line.split('fold along ')[1])
        else:
            x, y = line.split(',')
            coordinates.add((int(x), int(y)))

    for f in folds:
        fold_axis, fold_val = f.split('=')
        fold_val = int(fold_val)
        if fold_axis == 'y':
            for coord in coordinates.copy():
                if coord[1] >= fold_val:
                    coordinates.remove((coord[0], coord[1]))
                    coordinates.add((coord[0], fold_val - coord[1] + fold_val))
        elif fold_axis == 'x':
            for coord in coordinates.copy():
                if coord[0] >= fold_val:
                    coordinates.remove((coord[0], coord[1]))
                    coordinates.add((fold_val - coord[0] + fold_val, coord[1]))
        break
    return len(coordinates)


def part2(puzzle_input):
    coordinates = set()
    folds = []
    for line in puzzle_input:
        if line == '':
            continue
        elif 'fold along' in line:
            folds.append(line.split('fold along ')[1])
        else:
            x, y = line.split(',')
            coordinates.add((int(x), int(y)))

    for f in folds:
        fold_axis, fold_val = f.split('=')
        fold_val = int(fold_val)
        if fold_axis == 'y':
            for coord in coordinates.copy():
                if coord[1] >= fold_val:
                    coordinates.remove((coord[0], coord[1]))
                    coordinates.add((coord[0], fold_val - coord[1] + fold_val))
        elif fold_axis == 'x':
            for coord in coordinates.copy():
                if coord[0] >= fold_val:
                    coordinates.remove((coord[0], coord[1]))
                    coordinates.add((fold_val - coord[0] + fold_val, coord[1]))
    max_x = max(coordinates, key=lambda c: c[0])[0]
    max_y = max(coordinates, key=lambda c: c[1])[1]
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in coordinates:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    return 'See output above'


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
