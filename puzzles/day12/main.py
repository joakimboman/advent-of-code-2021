import os
from utils.file_reader import FileReader


def part1(puzzle_input):
    connections = {}
    for line in puzzle_input:
        nodes = line.split('-')
        if nodes[0] in connections:
            connections[nodes[0]].append(nodes[1])
        else:
            connections[nodes[0]] = [nodes[1]]
        if nodes[1] in connections:
            connections[nodes[1]].append(nodes[0])
        else:
            connections[nodes[1]] = [nodes[0]]
    num_paths = 0
    paths = [['start']]
    while paths:
        path = paths.pop(0)
        node = path[-1]
        for neighbour in connections[node]:
            if neighbour == 'end':
                num_paths += 1
            elif neighbour != 'start' and not (neighbour[0].islower() and neighbour in path):
                new_path = path.copy()
                new_path.append(neighbour)
                paths.append(new_path)

    return num_paths


def has_visited_small_cave_twice(path):
    small_caves = [x for x in path if x[0].islower() and x != 'start']
    return len(set(small_caves)) < len(small_caves)


def part2(puzzle_input):
    connections = {}
    for line in puzzle_input:
        nodes = line.split('-')
        if nodes[0] in connections:
            connections[nodes[0]].append(nodes[1])
        else:
            connections[nodes[0]] = [nodes[1]]
        if nodes[1] in connections:
            connections[nodes[1]].append(nodes[0])
        else:
            connections[nodes[1]] = [nodes[0]]
    num_paths = 0
    paths = [['start']]
    while paths:
        path = paths.pop(0)
        node = path[-1]
        for neighbour in connections[node]:
            if neighbour == 'end':
                num_paths += 1
            elif neighbour != 'start' and \
                    not (neighbour[0].islower() and neighbour in path and has_visited_small_cave_twice(path)):
                new_path = path.copy()
                new_path.append(neighbour)
                paths.append(new_path)

    return num_paths


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
