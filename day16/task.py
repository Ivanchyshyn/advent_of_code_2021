from inspect import isfunction

from utils import TYPE_TO_OPERATION

LITERAL_TYPE_ID = 4


def parse_input():
    with open('day16/input.txt') as fp:
        line = bin(int(fp.read().strip(), 16))[2:]
    mod = len(line) % 4
    if mod:
        zeros_to_add = 4 - mod
        line = '0' * zeros_to_add + line
    return line


class Resolve:
    def __init__(self):
        self.versions_total = 0

    def start_parsing(self, line, result):
        version, type_id = int(line[:3], 2), int(line[3:6], 2)
        self.versions_total += version

        line = line[6:]
        read = 6
        cur_res = []
        if type_id == LITERAL_TYPE_ID:
            read += self.parse_literal_type(line, cur_res)
            # Literal returns only 1 number
            cur_res = cur_res[0]
        else:
            # Set operation func on next sub-packets
            result.append(TYPE_TO_OPERATION[type_id])
            read += self.parse_operator_type(line, cur_res)
        result.append(cur_res)
        return read

    def parse_literal_type(self, line, result):
        found_zero = False
        bits = ''
        read = 0
        while line and not found_zero:
            if line[0] == '0':
                found_zero = True
            bits += line[1:5]
            line = line[5:]
            read += 5
        result.append(int(bits, 2))
        return read

    def parse_operator_type(self, line, result):
        length_type_id = line[0]
        line = line[1:]
        read = 1
        if length_type_id == '0':
            max_bits = int(line[:15], 2)
            line = line[15:]
            read += 15
            read += self.check_all_bits(line[:max_bits], result)
        else:
            max_packets = int(line[:11], 2)
            line = line[11:]
            read += 11
            read += self.check_packets(line, max_packets, result)
        return read

    def check_all_bits(self, line, result):
        bites_read = 0
        while line:
            read = self.start_parsing(line, result)
            bites_read += read
            line = line[read:]
        return bites_read

    def check_packets(self, line, max_packets, result):
        bits_read = 0
        for i in range(max_packets):
            read = self.start_parsing(line, result)
            bits_read += read
            line = line[read:]
        return bits_read

    def get_result(self, result):
        return next(self.unpack_result(result))

    def unpack_result(self, arr):
        i = 0
        while i < len(arr):
            value = arr[i]
            if isinstance(value, int):
                yield value
            elif isfunction(value):
                yield value(self.unpack_result(arr[i + 1]))
                i += 1
            i += 1


def solve_task1():
    line = parse_input()
    resolve = Resolve()
    resolve.start_parsing(line, [])
    return resolve.versions_total


def solve_task2():
    line = parse_input()
    result = []
    resolve = Resolve()
    resolve.start_parsing(line, result)
    return resolve.get_result(result)


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
