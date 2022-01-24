import os
from utils.file_reader import FileReader


def part1(puzzle_input):
    segments = {2: 1, 3: 7, 4: 4, 7: 8}
    num_easy_digits = 0

    for line in puzzle_input:
        output_values = line.split('| ')[1].split(' ')
        for v in output_values:
            if len(v) in segments:
                num_easy_digits += 1

    return num_easy_digits


def part2(puzzle_input):
    segments = {2: ['1'], 3: ['7'], 4: ['4'], 5: ['2', '3', '5'], 6: ['0', '6', '9'], 7: ['8']}
    sum_all_output_values = 0

    for line in puzzle_input:
        entries = line.split(' | ')
        signal_patterns = {}
        signals = entries[0].split(' ')
        digit_one = ''
        digit_four = ''
        digit_seven = ''
        digit_eight = ''
        for signal in signals:
            if len(signal) == 2:
                digit_one = signal
            if len(signal) == 3:
                digit_seven = signal
            if len(signal) == 4:
                digit_four = signal
            if len(signal) == 7:
                digit_eight = list(signal)

        signal_patterns['3'] = list(digit_seven)
        signal_patterns['5'] = list(set(digit_four).difference(digit_one))
        signal_patterns['9'] = list(set(digit_seven).union(signal_patterns['5']))
        signal_patterns['0'] = list(set(digit_eight).difference(digit_four).union(digit_seven))
        output_values = entries[1].split(' ')
        output_values_number = ''
        for output_value in output_values:
            output_value_digit = None
            segment = segments[len(output_value)]
            if len(segment) == 1:
                output_value_digit = segment[0]
            else:
                for s in segment:
                    if s in signal_patterns:
                        char_list = signal_patterns[s]
                        if all(c in output_value for c in char_list):
                            output_value_digit = s
                if not output_value_digit:
                    if len(output_value) == 5:
                        output_value_digit = '2'
                    else:
                        output_value_digit = '6'
            output_values_number += output_value_digit

        sum_all_output_values += int(output_values_number)
    return sum_all_output_values


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
