def solve_task1():
    total = 0
    with open('day1/input.txt') as fp:
        prev_line = int(next(fp).strip())
        for line in fp:
            line = int(line.strip())
            if line > prev_line:
                total += 1
            prev_line = line
    return total


def solve_task2():
    total = 0
    with open('day1/input.txt') as fp:
        prev_summary = None
        first = second = None
        while True:
            try:
                third = int(next(fp).strip())
            except StopIteration:
                break

            if first is None or second is None:
                first, second = second, third
                continue

            summary = first + second + third
            if prev_summary is not None and summary > prev_summary:
                total += 1
            prev_summary = summary
            first, second = second, third
    return total


if __name__ == '__main__':
    result1 = solve_task1()
    result2 = solve_task2()
    print('task 1 -', result1)
    print('task 2 -', result2)
