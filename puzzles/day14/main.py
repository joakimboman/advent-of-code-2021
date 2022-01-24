import os
from utils.file_reader import FileReader


def solution(puzzle_input, steps):
    polymer_template = {}
    rules = {}
    count = {}
    for line in puzzle_input:
        if '->' in line:
            key, val = line.split(' -> ')
            rules[key] = [key[0] + val, val + key[1]]
        elif line != '':
            for i, char in enumerate(line):
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
                if i + 1 < len(line):
                    pair = char + line[i + 1]
                    if pair in polymer_template:
                        polymer_template[pair] += 1
                    else:
                        polymer_template[pair] = 1
    for _ in range(steps):
        new_polymer = {}
        for key in polymer_template:
            occurrences = polymer_template[key]
            new_pairs = rules[key]
            new_char = new_pairs[0][1]
            if new_char in count:
                count[new_char] += occurrences
            else:
                count[new_char] = occurrences
            for pair in new_pairs:
                if pair in new_polymer:
                    new_polymer[pair] += occurrences
                else:
                    new_polymer[pair] = occurrences
        polymer_template = new_polymer

    return max(count.items(), key=lambda x: x[1])[1] - min(count.items(), key=lambda x: x[1])[1]


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {solution(puzzle_input, 10)}")
    print(f"Part 2: {solution(puzzle_input, 40)}")
