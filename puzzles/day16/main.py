import math
import os
from utils.file_reader import FileReader


def get_binary_from_hex(puzzle_input):
    hex_to_binary = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    binary = ''
    for i in puzzle_input[0]:
        binary += hex_to_binary[i]
    return binary


def read_packet_part1(binary, current_bit):
    version = binary[current_bit + 0] + binary[current_bit + 1] + binary[current_bit + 2]
    version_in_decimal = int(version, 2)

    bits_read = 0
    type_id = binary[current_bit + 3] + binary[current_bit + 4] + binary[current_bit + 5]
    if type_id == '100':
        is_not_last_group = True
        current_bit += 6
        bits_read += 6

        while is_not_last_group:
            first_bit = binary[current_bit]

            current_bit += 5
            bits_read += 5
            if first_bit == '0':
                is_not_last_group = False

    else:
        length_type_id = binary[current_bit + 6]
        if length_type_id == '0':
            length_in_bits = ''
            for i in range(15):
                length_in_bits += binary[current_bit + 7 + i]
            length_in_bits_decimal = int(length_in_bits, 2)

            current_bit += 22
            while bits_read < length_in_bits_decimal:
                version, bits = read_packet_part1(binary, current_bit)
                version_in_decimal += version
                current_bit += bits
                bits_read += bits
            bits_read += 22

        elif length_type_id == '1':
            number_of_sub_packets = ''
            for i in range(11):
                number_of_sub_packets += binary[current_bit + 7 + i]
            number_of_sub_packets_decimal = int(number_of_sub_packets, 2)

            current_bit += 18
            packets_read = 0
            while packets_read < number_of_sub_packets_decimal:
                version, bits = read_packet_part1(binary, current_bit)
                version_in_decimal += version
                current_bit += bits
                bits_read += bits
                packets_read += 1
            bits_read += 18

    return version_in_decimal, bits_read


def part1(puzzle_input):
    binary = get_binary_from_hex(puzzle_input)
    version, _ = read_packet_part1(binary, 0)
    return version


def handle_values_part2(values, type_id):
    if type_id == 0:
        return sum(values)
    elif type_id == 1:
        return math.prod(values)
    elif type_id == 2:
        return min(values)
    elif type_id == 3:
        return max(values)
    elif type_id == 5:
        if values[0] > values[1]:
            return 1
        else:
            return 0
    elif type_id == 6:
        if values[0] < values[1]:
            return 1
        else:
            return 0
    elif type_id == 7:
        if values[0] == values[1]:
            return 1
        else:
            return 0
    return None


def read_packet_part2(binary, current_bit):
    bits_read = 0
    type_id_decimal = int(binary[current_bit + 3] + binary[current_bit + 4] + binary[current_bit + 5], 2)

    if type_id_decimal == 4:
        is_not_last_group = True
        current_bit += 6
        bits_read += 6

        literal_value = ''
        while is_not_last_group:
            first_bit = binary[current_bit]
            for i in range(1, 5):
                literal_value += binary[current_bit + i]
            current_bit += 5
            bits_read += 5
            if first_bit == '0':
                is_not_last_group = False

        literal_value_decimal = int(literal_value, 2)

    else:
        values = []
        length_type_id = binary[current_bit + 6]
        if length_type_id == '0':

            length_in_bits = ''
            for i in range(15):
                length_in_bits += binary[current_bit + 7 + i]
            length_in_bits_decimal = int(length_in_bits, 2)

            current_bit += 22
            while bits_read < length_in_bits_decimal:
                value, bits = read_packet_part2(binary, current_bit)
                values.append(value)
                current_bit += bits
                bits_read += bits
            bits_read += 22

        elif length_type_id == '1':

            number_of_sub_packets = ''
            for i in range(11):
                number_of_sub_packets += binary[current_bit + 7 + i]
            number_of_sub_packets_decimal = int(number_of_sub_packets, 2)

            current_bit += 18
            packets_read = 0

            while packets_read < number_of_sub_packets_decimal:
                value, bits = read_packet_part2(binary, current_bit)
                values.append(value)
                current_bit += bits
                bits_read += bits
                packets_read += 1
            bits_read += 18

        literal_value_decimal = handle_values_part2(values, type_id_decimal)

    return literal_value_decimal, bits_read


def part2(puzzle_input):
    binary = get_binary_from_hex(puzzle_input)
    values, _ = read_packet_part2(binary, 0)
    return values


def run(input_file):
    puzzle_input = FileReader.read_input_file(os.path.dirname(__file__), f"inputs/{input_file}")
    puzzle_input = [x.rstrip() for x in puzzle_input]
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
