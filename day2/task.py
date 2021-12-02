def solve_task1():
    forward = depth = 0
    with open('day2/input.txt') as fp:
        for line in fp:
            command, value = line.strip().split(maxsplit=1)
            value = int(value)
            if command == 'forward':
                forward += value
            else:
                depth += value if command == 'down' else -value

    return forward * depth


def solve_task2():
    forward = depth = aim = 0
    with open('day2/input.txt') as fp:
        for line in fp:
            command, value = line.strip().split(maxsplit=1)
            value = int(value)
            if command == 'forward':
                forward += value
                depth += aim * value
            else:
                aim += value if command == 'down' else -value

    return forward * depth


if __name__ == '__main__':
    result1 = solve_task1()
    result2 = solve_task2()
    print('task 1 -', result1)
    print('task 2 -', result2)
