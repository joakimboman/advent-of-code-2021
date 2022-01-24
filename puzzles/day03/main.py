import os
from utils.file_reader import FileReader


def part1(puzzle_input):
    most_common_bits = []
    for binary in puzzle_input:
        for i in range(len(binary)):
            if len(most_common_bits) < len(binary):
                if int(binary[i]) == 1:
                    most_common_bits.append(1)
                else:
                    most_common_bits.append(-1)
            else:
                if int(binary[i]) == 1:
                    most_common_bits[i] += 1
                else:
                    most_common_bits[i] -= 1

    gamma = []
    for bit in most_common_bits:
        if bit < 0:
            gamma.append(str(0))
        else:
            gamma.append(str(1))
    gamma_str = ''.join(gamma)
    epsilon = gamma_str.replace('1', '2').replace('0', '1').replace('2', '0')
    decimal_gamma = int(gamma_str, 2)
    decimal_epsilon = int(epsilon, 2)
    return decimal_gamma * decimal_epsilon


def get_bit_difference(binaries, bit_index):
    diff = 0
    for binary in binaries:
        if int(binary[bit_index]) == 1:
            diff += 1
        else:
            diff -= 1
    return diff


def part2(puzzle_input):
    oxygen_generator_rating = puzzle_input[:]
    co2_scrubber_rating = puzzle_input[:]
    max_bit_index = len(puzzle_input[0])
    for i in range(max_bit_index):
        if len(oxygen_generator_rating) == 1 and len(co2_scrubber_rating) == 1:
            break

        diff_oxygen_generator_rating = get_bit_difference(oxygen_generator_rating, i)
        if diff_oxygen_generator_rating >= 0:
            most_common_bit = 1
        else:
            most_common_bit = 0

        diff_co2_scrubber_rating = get_bit_difference(co2_scrubber_rating, i)
        if diff_co2_scrubber_rating >= 0:
            least_common_bit = 0
        else:
            least_common_bit = 1

        for binary in oxygen_generator_rating[:]:
            if len(oxygen_generator_rating) == 1:
                continue
            if int(binary[i]) != most_common_bit:
                oxygen_generator_rating.remove(binary)

        for binary in co2_scrubber_rating[:]:
            if len(co2_scrubber_rating) == 1:
                continue
            if int(binary[i]) != least_common_bit:
                co2_scrubber_rating.remove(binary)

    decimal_oxygen_generator_rating = int(oxygen_generator_rating[0], 2)
    decimal_co2_scrubber_rating = int(co2_scrubber_rating[0], 2)
    return decimal_oxygen_generator_rating * decimal_co2_scrubber_rating


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
