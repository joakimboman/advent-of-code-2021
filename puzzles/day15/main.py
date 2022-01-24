import heapq
import os
import sys
from utils.file_reader import FileReader


def part1(puzzle_input):
    input_matrix = {}
    for x, line in enumerate(puzzle_input):
        for y, risk in enumerate(line):
            input_matrix[(x, y)] = int(risk)

    max_x = max(input_matrix.keys(), key=lambda t: t[0])[0]
    max_y = max(input_matrix.keys(), key=lambda t: t[1])[1]
    risk_graph = {}
    risk_paths = {}
    for (i, j) in input_matrix:
        risk_paths[(i, j)] = sys.maxsize
        neighbours = {}
        if i - 1 >= 0:
            neighbours[(i - 1, j)] = input_matrix[(i - 1, j)]
        if i + 1 <= max_x:
            neighbours[(i + 1, j)] = input_matrix[(i + 1, j)]
        if j - 1 >= 0:
            neighbours[(i, j - 1)] = input_matrix[(i, j - 1)]
        if j + 1 <= max_y:
            neighbours[(i, j + 1)] = input_matrix[(i, j + 1)]
        risk_graph[(i, j)] = neighbours

    risk_paths[(0, 0)] = 0
    priority_queue = [(0, (0, 0))]
    while priority_queue:
        current_path, current_node = heapq.heappop(priority_queue)
        if current_path <= risk_paths[current_node]:
            for neighbour, risk in risk_graph[current_node].items():
                risk_path = current_path + risk
                if risk_path < risk_paths[neighbour]:
                    risk_paths[neighbour] = risk_path
                    heapq.heappush(priority_queue, (risk_path, neighbour))

    return risk_paths[(max_x, max_y)]


def part2(puzzle_input):
    input_matrix = {}
    for x, line in enumerate(puzzle_input):
        for y, risk in enumerate(line):
            input_matrix[(x, y)] = int(risk)

    max_x = max(input_matrix.keys(), key=lambda t: t[0])[0] + 1
    max_y = max(input_matrix.keys(), key=lambda t: t[1])[1] + 1
    for i in range(5):
        for j in range(5):
            if i == 0 and j == 0:
                continue
            for x in range(max_x):
                for y in range(max_y):
                    risk = input_matrix[(x, y)]
                    while risk + i + j > 9:
                        risk -= 9
                    input_matrix[(x + max_x * i, y + max_y * j)] = risk + i + j

    risk_graph = {}
    risk_paths = {}
    for (i, j) in input_matrix:
        risk_paths[(i, j)] = sys.maxsize
        neighbours = {}
        if i - 1 >= 0:
            neighbours[(i - 1, j)] = input_matrix[(i - 1, j)]
        if i + 1 < max_x * 5:
            neighbours[(i + 1, j)] = input_matrix[(i + 1, j)]
        if j - 1 >= 0:
            neighbours[(i, j - 1)] = input_matrix[(i, j - 1)]
        if j + 1 < max_y * 5:
            neighbours[(i, j + 1)] = input_matrix[(i, j + 1)]
        risk_graph[(i, j)] = neighbours

    risk_paths[(0, 0)] = 0
    priority_queue = [(0, (0, 0))]
    while priority_queue:
        current_path, current_node = heapq.heappop(priority_queue)
        if current_path <= risk_paths[current_node]:
            for neighbour, risk in risk_graph[current_node].items():
                risk_path = current_path + risk
                if risk_path < risk_paths[neighbour]:
                    risk_paths[neighbour] = risk_path
                    heapq.heappush(priority_queue, (risk_path, neighbour))
    return risk_paths[(max_x * 5 - 1, max_y * 5 - 1)]


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
