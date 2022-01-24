import copy
import json
import math
import os
import sys

from utils.file_reader import FileReader


class Node:
    def __init__(self, left, right, value, depth=None):
        self.left = left
        self.right = right
        self.value = value
        self.depth = depth

    def flatten(self, list_of_nodes):
        if self.left:
            self.left.flatten(list_of_nodes)

        if self.value is not None:
            list_of_nodes.append((self.value, self.depth))

        if self.right:
            self.right.flatten(list_of_nodes)
        return list_of_nodes


def create_tree(input_list, depth):
    if isinstance(input_list, list):
        return Node(create_tree(input_list[0], depth + 1), create_tree(input_list[1], depth + 1), None, depth)
    else:
        return Node(None, None, input_list, depth)


def explode(flat_tree, tree_start_depth):
    for i, (value, depth) in enumerate(flat_tree.copy()):
        if abs(tree_start_depth - depth) >= 4:
            if i - 1 >= 0:
                (left_of_exploding_v, left_of_exploding_d) = flat_tree[i - 1]
                flat_tree[i - 1] = (left_of_exploding_v + value, left_of_exploding_d)
            if i + 2 < len(flat_tree):
                (explode_pair_v, explode_pair_d) = flat_tree[i + 1]
                (right_of_exploding_v, right_of_exploding_d) = flat_tree[i + 2]
                flat_tree[i + 2] = (right_of_exploding_v + explode_pair_v, right_of_exploding_d)
            flat_tree[i] = (0, depth - 1)
            flat_tree.pop(i + 1)
            return True

    return False


def split(flat_tree):
    for i, (value, depth) in enumerate(flat_tree.copy()):
        if value >= 10:
            left = math.floor(value / 2)
            right = math.ceil(value / 2)
            flat_tree[i] = (left, depth + 1)
            flat_tree.insert(i + 1, (right, depth + 1))
            return True
    return False


def magnitude(flat_tree, max_depth):
    remove_index = []
    for i, (value, depth) in enumerate(flat_tree):
        if i + 1 == len(flat_tree):
            continue

        if depth == max_depth and i not in remove_index:
            (next_v, next_d) = flat_tree[i + 1]
            flat_tree[i] = (3 * value + 2 * next_v, depth - 1)
            remove_index.append(i + 1)

    remove_index.reverse()
    for i in remove_index:
        flat_tree.pop(i)


def part1(puzzle_input):
    snailfish_numbers = []
    for line in puzzle_input:
        snailfish_numbers.append(json.loads(line))

    tree = create_tree(snailfish_numbers[0], 0)
    flat_tree = tree.flatten([])
    current_start_depth = 0
    for i, _ in enumerate(snailfish_numbers[1:]):
        if i + 1 == len(snailfish_numbers):
            continue
        current_tree = create_tree(snailfish_numbers[i + 1], current_start_depth)
        current_flat_tree = current_tree.flatten([])
        flat_tree += current_flat_tree
        did_explode = did_split = True
        while did_explode or did_split:
            did_explode = explode(flat_tree, current_start_depth)
            if not did_explode:
                did_split = split(flat_tree)
        current_start_depth -= 1

    while len(flat_tree) > 1:
        max_depth = max(flat_tree, key=lambda t: t[1])[1]
        magnitude(flat_tree, max_depth)
    return flat_tree[0][0]


def part2(puzzle_input):
    snailfish_numbers = []
    for line in puzzle_input:
        snailfish_numbers.append(json.loads(line))

    max_magnitude = -sys.maxsize
    for i, number in enumerate(snailfish_numbers):
        tree = create_tree(number, 0)
        orig_flat_tree = tree.flatten([])
        for j, _ in enumerate(snailfish_numbers):
            if j == i:
                continue
            flat_tree = copy.deepcopy(orig_flat_tree)
            current_tree = create_tree(snailfish_numbers[j], 0)
            current_flat_tree = current_tree.flatten([])
            flat_tree += current_flat_tree
            did_explode = did_split = True
            while did_explode or did_split:
                did_explode = explode(flat_tree, 0)
                if not did_explode:
                    did_split = split(flat_tree)

            while len(flat_tree) > 1:
                max_depth = max(flat_tree, key=lambda t: t[1])[1]
                magnitude(flat_tree, max_depth)

            if flat_tree[0][0] > max_magnitude:
                max_magnitude = flat_tree[0][0]

    return max_magnitude


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
