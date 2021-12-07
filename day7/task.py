
def solve_task1():
    with open('day7/input.txt') as fp:
        crabs = list(map(int, fp.read().strip().split(',')))
    minimum, maximum = min(crabs), max(crabs)
    fuel = float('inf')
    for num in range(minimum, maximum + 1):
        res = sum(abs(x - num) for x in crabs)
        fuel = min(fuel, res)
    return fuel


def solve_task2():
    with open('day7/input.txt') as fp:
        crabs = list(map(int, fp.read().strip().split(',')))
    minimum, maximum = min(crabs), max(crabs)
    fuel = float('inf')
    for num in range(minimum, maximum + 1):
        res = sum(arithmetic_sum(abs(x - num)) for x in crabs)
        fuel = min(fuel, res)
    return fuel


def arithmetic_sum(n):
    return n * (n + 1) / 2


if __name__ == '__main__':
    result1 = solve_task1()
    result2 = solve_task2()
    print('task 1 -', result1)
    print('task 2 -', result2)
