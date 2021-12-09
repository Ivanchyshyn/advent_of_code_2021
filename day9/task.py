import heapq
import operator
from functools import reduce


def get_area():
    area = []
    with open('day9/input.txt') as fp:
        for line in fp:
            area.append(list(map(int, line.strip())))
    return area


def get_low_points_indexes(area):
    low_points = []
    rows, cols = len(area), len(area[0])
    for i in range(rows):
        for j in range(cols):
            if check_num(area, i, j):
                low_points.append((i, j))
    return low_points


def check_num(area, i, j):
    num = area[i][j]
    for x, y in valid_checks(area, i, j):
        if num >= area[x][y]:
            return False
    return True


def valid_checks(area, i, j):
    valid = []
    checks = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for x, y in checks:
        if -1 in (x, y):
            continue
        try:
             area[x][y]
        except IndexError:
            pass
        else:
            valid.append((x, y))
    return valid


def solve_task1():
    area = get_area()
    low_points_indexes = get_low_points_indexes(area)
    return sum(area[i][j] + 1 for i, j in low_points_indexes)


def solve_task2():
    area = get_area()
    low_points_indexes = get_low_points_indexes(area)
    result = []
    for i, j in low_points_indexes:
        visited = set()
        recursion(area, i, j, visited)
        result.append(len(visited))
    return reduce(operator.mul, heapq.nlargest(3, result))


def recursion(area, i, j, visited):
    num = area[i][j]
    visited.add((i, j))
    for x, y in valid_checks(area, i, j):
        new_num = area[x][y]
        if new_num == 9:
            continue
        if num < new_num:
            recursion(area, x, y, visited)


if __name__ == '__main__':
    result1 = solve_task1()
    print('task 1 -', result1)
    result2 = solve_task2()
    print('task 2 -', result2)
