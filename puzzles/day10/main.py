import os
from utils.file_reader import FileReader


def part1(puzzle_input):
    matching_parentheses = {')': '(', ']': '[', '}': '{', '>': '<'}
    illegal_chars_count = {')': 0, ']': 0, '}': 0, '>': 0}
    for line in puzzle_input:
        stack = []
        for char in line:
            if char == ')' or char == ']' or char == '}' or char == '>':
                if matching_parentheses[char] == stack[-1]:
                    stack.pop()
                else:
                    illegal_chars_count[char] += 1
                    break
            else:
                stack.append(char)
    return illegal_chars_count[')'] * 3 + illegal_chars_count[']'] * 57 + illegal_chars_count['}'] * 1197 + \
           illegal_chars_count['>'] * 25137


def part2(puzzle_input):
    matching_parentheses = {')': '(', ']': '[', '}': '{', '>': '<', '(': ')', '[': ']', '{': '}', '<': '>'}
    auto_complete_lines = []
    for line in puzzle_input:
        stack = []
        is_corrupt = False
        for char in line:
            if char == ')' or char == ']' or char == '}' or char == '>':
                if matching_parentheses[char] == stack[-1]:
                    stack.pop()
                else:
                    is_corrupt = True
                    break
            else:
                stack.append(char)
        if stack and not is_corrupt:
            auto_complete = []
            while stack:
                char = stack.pop()
                auto_complete.append(matching_parentheses[char])
            auto_complete_lines.append(auto_complete)

    scores = []
    char_points = {')': 1, ']': 2, '}': 3, '>': 4}
    for line in auto_complete_lines:
        score = 0
        for char in line:
            score *= 5
            score += char_points[char]
        scores.append(score)

    scores.sort()
    return scores[int((len(scores) - 1) / 2)]


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
