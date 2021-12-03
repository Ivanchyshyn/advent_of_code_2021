import operator


def solve_task1():
    res = []
    with open('day3/input.txt') as fp:
        for line in fp:
            for i, bit in enumerate(line.strip()):
                if i >= len(res):
                    res.append([0, 0])
                res[i][bit == '1'] += 1

    gamma = epsilon = ''
    for nums in res:
        maximum, minimum = max_and_min_indexes(nums)
        gamma += str(maximum)
        epsilon += str(minimum)
    return int(gamma, 2) * int(epsilon, 2)


def max_and_min_indexes(arr):
    num1, num2 = arr
    if num1 >= num2:
        return 0, 1
    return 1, 0


def solve_task2():
    with open('day3/input.txt') as fp:
        arr = fp.read().strip().split('\n')
    oxygen = find_common(arr, compare=operator.ge)
    co2 = find_common(arr, compare=operator.lt)
    return int(oxygen, 2) * int(co2, 2)


def find_common(arr, compare):
    width = len(arr[0])
    i = 0
    while len(arr) != 1 and i < width:
        ones, zeros = [], []
        for line in arr:
            if line[i] == '0':
                zeros.append(line)
            else:
                ones.append(line)
        if compare(len(ones), len(zeros)):
            arr = ones
        else:
            arr = zeros
        i += 1
    return arr[0]


if __name__ == '__main__':
    result1 = solve_task1()
    result2 = solve_task2()
    print('task 1 -', result1)
    print('task 2 -', result2)
